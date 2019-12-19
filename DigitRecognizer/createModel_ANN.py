#-*- coding: utf-8 -*-　
import numpy as np 
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import random
import math
from pandas import DataFrame
from time import time

def layer_debug(output_dim, input_dim, inputs, outputname, activation=None):
	W = tf.Variable(tf.random_normal([input_dim, output_dim]))
	b = tf.Variable(tf.random_normal([1, output_dim]))
	XWb = tf.matmul(inputs,W,name=outputname)+b
	if activation is None:
		outputs = XWb
	else:
		outputs = activation(XWb)
	return outputs,W,b

def next_batch(data, batchSize):
	random.shuffle(data)
	batch_x = []; batch_y = []
	batch = data[0:batchSize]
	for a in batch:
		batch_y.append(a[0:1])
		batch_x.append(a[1:])
	return np.array(batch_x), np.array(batch_y)

def convert_to_one_hot(np_array, numLimit):
	rCount = len(np_array)
	re_np_array = np.zeros((rCount, numLimit))
	re_np_array[np.arange(rCount), np_array] = 1
	return re_np_array

def splitXY(data):
	_x = []; _y = [];
	for a in data:
		_y.append(a[0:1]); _x.append(a[1:]);
	return np.array(_x), np.array(_y)

if __name__ == '__main__':		
	homefolder = "D:\\AI_Train\\Kaggle\\DigitRecognizer\\"
	modelFile = homefolder+'Model\\model.ckpt'
	
	################# loading and split validation data #################
	df_row = pd.read_csv("train.csv")
	featureCount = len(df_row.columns)-1
	rowData = df_row.values.tolist()	
	random.shuffle(rowData)
	valCount = int(math.floor(len(rowData)*0.2))	# 20% for validation data, 80%  for training data
	valData = rowData[0:valCount]
	valData_x, valData_y = splitXY(valData)
	traData = rowData[valCount:len(rowData)]
	traData_x, traData_y = splitXY(traData)		
	valData_y = convert_to_one_hot(valData_y.flatten(), 10)
	traData_y = convert_to_one_hot(traData_y.flatten(), 10)
	
	################# create model #################		
	x = tf.placeholder("float", [None, featureCount], name='x')
	h1,W1,b1 = layer_debug(output_dim=256, input_dim=featureCount, inputs=x, outputname='h1_layer', activation=tf.nn.relu)
	h2,W2,b2 = layer_debug(output_dim=256, input_dim=256, inputs=h1, outputname='h2_layer', activation=tf.nn.relu)
	y_predict,W3,b3 = layer_debug(output_dim=10, input_dim=256, inputs=h2, outputname='output_layer')	
	
	################# training #################
	trainEpochs = 50
	batchSize = 200
	last_acc = 0
	totalBachs = math.ceil(len(traData)/batchSize)
	#loss_list = []; epoch_list = []; accuracy_list = []	
	
	y_label = tf.placeholder("float", [None, 10])	
	loss_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y_predict, labels=y_label))		
	accu_function = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y_label, 1), tf.argmax(y_predict, 1)), "float"))
	optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss_function)			
	saver = tf.train.Saver()
	
	startTime = time()		
	with tf.Session() as sess:
		init = tf.global_variables_initializer()
		sess.run(init)
		for epoch in range(trainEpochs):						
			for i in range(totalBachs):
				batch_x, batch_y = next_batch(traData, batchSize)											
				sess.run(optimizer,feed_dict={x: traData_x, y_label: traData_y})			
			loss,acc = sess.run([loss_function, accu_function],feed_dict={x: valData_x, y_label: valData_y})			
			#loss_list.append(loss); epoch_list.append(epoch); accuracy_list.append(acc) 			
			print("Train Epoch:", '%02d' %(epoch+1), "Loss=", "{:.9f}".format(loss)," Accuracy=",acc)			
			
			if acc > last_acc:
				last_acc = acc
				save_path = saver.save(sess, modelFile)
			else:
				break
			
		duration = time() - startTime
		print("Train Finish takes: ", duration)			
			

	