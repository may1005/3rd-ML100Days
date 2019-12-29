import os
import re
import random
import pickle
import tensorflow as tf
import numpy as np
from time import time
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"   # 1：默認顯示等级(顯示所有信息)，2；只顯示WARNING與ERROR，3；只顯示ERROR
#os.environ["CUDA_VISIBLE_DEVICES"] = '1'   # 使用第2張GPU卡(經測試發現較0(cpu)快)

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

def display_test_Sentiment(test_text, y_test, predict, i):
	SentimentDist = {1:'負面的',0:'正面的'}
	print(test_text[i])
	print('label真實值:', SentimentDist[y_test[i]], '預測結果:', SentimentDist[predict[i]])

if __name__ == '__main__':
	startTime = time()	
	homefolder = "D:\\AI_Train\\IMDB\\"	
	modelFile = homefolder+'Model\\model_RNN.h5'		
	tokenFile = homefolder+'Model\\tokenizer.pickle'
	predictFile = homefolder+'Output\\PredResult.csv'
	
	################# 參數設定 #################
	FeatureNum = 100			# 固定文本詞彙數，需與createModel_RNN.py相同
	
	################# test資料讀入與字典讀入 #################
	y_test, test_text = read_files(homefolder, "test")	
	token = pickle.load(open(tokenFile, 'rb'))
	#word_index = token.word_index	
	#print(dict(list(word_index.items())[0:100]))		#列出前100名出現的詞彙
	
	################# test資料-->數字-->向量數字 #################
	x_test_seq = token.texts_to_sequences(test_text)
	x_test = sequence.pad_sequences(x_test_seq, maxlen=FeatureNum)
	
	################# 讀取模型並列出測試準度 #################
	model = tf.contrib.keras.models.load_model(modelFile)
	scores = model.evaluate(x_test, y_test, verbose=0)		
	print('Test accuracy:', scores[1])
	
	################# 進行預測，輸出預測結果 #################
	predict = model.predict_classes(x_test)
	predict = predict.reshape(-1)	
	display_test_Sentiment(test_text, y_test, predict, 5)
	
	################# 預測結果寫檔 #################
	f = open(predictFile, "w")			
	title = "POSorNeg\n"
	f.write(title)		
	for i in range(0, len(predict)):
		result = str(predict[i])+"\n"
		f.write(result)
	f.close()	
	
	duration = time() - startTime
	print("Train Finish takes: ", duration)
	
	
	
	
	
	
	
	
	
	
	