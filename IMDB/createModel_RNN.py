import collections
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd
import re
import os
import random
import math
import pickle
from time import time
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Flatten
from tensorflow.keras.callbacks import EarlyStopping

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"   # 1：默認顯示等级(顯示所有信息)，2；只顯示WARNING與ERROR，3；只顯示ERROR
#os.environ["CUDA_VISIBLE_DEVICES"] = '1'   # 使用第2張GPU卡(經測試發現較0快)

def rm_tags(text):
	re_tag = re.compile(r'<[^>]+>')
	return re_tag.sub('', text)
	
def read_files(homefolder, filetype):
	path = homefolder + "aclImdb\\"
	file_list = []
	pos_path = path + filetype + "/pos/"
	for f in os.listdir(pos_path):
		file_list+=[pos_path+f]
	neg_path = path + filetype + "/neg/"
	for f in os.listdir(neg_path):
		file_list+=[neg_path+f]
	print('read', filetype, 'file:', len(file_list))
	all_labels = ([1] * 12500 + [0] * 12500)
	all_texts = []
	for fi in file_list:
		with open(fi, encoding = "utf8") as file_input:
			all_texts += [rm_tags(" ".join(file_input.readlines()))]
	return all_labels, all_texts

if __name__ == '__main__':
	startTime = time()
	
	################# 檔案路徑設定 #################
	homefolder = "D:\\AI_Train\\IMDB\\"	
	modelFile = homefolder+'Model\\model_RNN.h5'
	tokenFile = homefolder+'Model\\tokenizer.pickle'
	
	################# 參數設定 #################
	ValidNumPrecent = 0.2		# Validation 百分比
	TokenWordNum = 2000			# 字典數量
	FeatureNum = 100			# 固定文本詞彙數
	BatchSize=100				# batch_size大小
	Epochs=10					# epochs次數
	
	y_train, train_text = read_files(homefolder, "train")	
	
	################# 建立字典庫 #################
	token = Tokenizer(num_words=TokenWordNum)
	token.fit_on_texts(train_text)	
	pickle.dump(token, open(tokenFile, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
	#word_index = token.word_index
	#print(dict(list(word_index.items())[0:100]))		#列出前100名出現的詞彙
	#print(np.array(train_text).shape, np.array(y_train).shape)  #檢視維度
	
	################# 將詞彙對應到數字 #################
	x_train_seq = token.texts_to_sequences(train_text)	
	#print(np.array(x_train_seq).shape)    #檢視維度
	
	################# 將詞彙數量保持在一固定詞彙數(固定欄位數) #################
	x_train = sequence.pad_sequences(x_train_seq, maxlen=FeatureNum)	
	#print(np.array(x_train).shape)    #檢視維度
	
	
	################# 建立模型 #################
	model=Sequential()	
	#---------------- Embedding層，Dropout避免overfiting ----------------#
	model.add(Embedding(output_dim=32, input_dim=TokenWordNum, input_length=FeatureNum))
	model.add(Dropout(0.2))
	
	#---------------- LSTM層，Dropout避免overfiting ----------------#
	#model.add(Flatten())
	model.add(LSTM(100))
	model.add(Dropout(0.2))	
	
	#---------------- 隱藏層，Dropout避免overfiting ----------------#
	model.add(Dense(256, activation='relu'))
	model.add(Dropout(0.2))
	
	#---------------- 輸出層 ----------------#
	model.add(Dense(1, activation='sigmoid'))
	#print(model.summary())
	
	################# 模型訓練與結果儲存 #################
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	early_stopping = EarlyStopping(monitor='val_acc', patience=8, verbose=2)
	model.fit(x_train, y_train, batch_size=BatchSize, epochs=Epochs, validation_split=0.2, callbacks=[early_stopping])	
	model.save(modelFile)
	
	duration = time() - startTime
	print("Train Finish takes: ", duration)
	
	
	
	
	
	
	
	