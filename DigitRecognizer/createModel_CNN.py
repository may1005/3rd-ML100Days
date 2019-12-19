#-*- coding: utf-8 -*-　
import numpy as np 
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"
import tensorflow as tf
import random
import math
from pandas import DataFrame
from time import time

def buildConAndPoolLayer(lastLayer, fTPar, b_shape, Conv2dStrides, poolKsize, poolStrides, w_name, b_name, p_name):	
	W = tf.Variable(tf.truncated_normal(fTPar, stddev=0.1), name=w_name)
	b = tf.Variable(tf.constant(0.1, shape=b_shape), name=b_name)
	Conv2d = tf.nn.conv2d(lastLayer, W, strides=Conv2dStrides, padding='SAME')+b
	Conv = tf.nn.relu(Conv2d)
	Pool = tf.nn.max_pool(Conv, ksize=poolKsize, strides=poolStrides, padding='SAME', name=p_name)
	return W, b, Pool

def buildHiddenLayer(d_Flat, h_shape, b_shape, k_prob, w_name, b_name, h_name):
	W = tf.Variable(tf.truncated_normal(h_shape, stddev=0.1), name=w_name)
	b = tf.Variable(tf.constant(0.1, shape=b_shape), name=b_name)
	d_hidden = tf.nn.relu(tf.matmul(d_Flat, W)+b)
	d_hidden_trop = tf.nn.dropout(d_hidden, keep_prob=k_prob, name=h_name);
	return W, b, d_hidden_trop

def buildOutputLayer(h_layer, out_shape, b_shape):
	W = tf.Variable(tf.truncated_normal(out_shape, stddev=0.1), name='OutputLayer_W')
	b = tf.Variable(tf.constant(0.1, shape=b_shape), name='OutputLayer_b')
	y_predict = tf.nn.softmax(tf.matmul(h_layer, W, name='OutputLayer')+b)
	return W, b, y_predict

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
	modelFile = homefolder+'Model\\model_CNN.ckpt'
	
	################# loading and split validation data #################
	df_row = pd.read_csv("train.csv")
	featureCount = len(df_row.columns)-1
	featureSQRT = int(math.sqrt(featureCount))	
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
	tf.logging.set_verbosity(tf.logging.ERROR)		#ignore warning: colocate_with is deprecated
	x = tf.placeholder("float", [None, featureCount], name='x')		
	x_image = tf.reshape(x, [-1, featureSQRT, featureSQRT, 1])	
	
	W_1, b_1, pool_1 = buildConAndPoolLayer(x_image, fTPar=[5,5,1,10], b_shape=[10], Conv2dStrides=[1,1,1,1], poolKsize=[1,2,2,1], poolStrides=[1,2,2,1], w_name='w1', b_name='b1', p_name='pool_1')
	W_2, b_2, pool_2 = buildConAndPoolLayer(pool_1, fTPar=[5,5,10,16], b_shape=[16], Conv2dStrides=[1,1,1,1], poolKsize=[1,2,2,1], poolStrides=[1,2,2,1], w_name='w2', b_name='b2', p_name='pool_2')
	
	flatNum = int(16*(featureSQRT/(2*2))*(featureSQRT/(2*2)))
	print("flatNum : "+str(flatNum))
	D_Flat = tf.reshape(pool_2, [-1, flatNum])		#平坦層，縮小一半，2層池化層=>2*2
	W_3, b_3, hidden_1 = buildHiddenLayer(D_Flat, h_shape=[flatNum, 128], b_shape=[128], k_prob=0.8, w_name='w3', b_name='b3', h_name='hidden_1')
	W_4, b_4, hidden_2 = buildHiddenLayer(hidden_1, h_shape=[128, 128], b_shape=[128], k_prob=0.8, w_name='w4', b_name='b4', h_name='hidden_2')
	W_5, b_5, y_predict = buildOutputLayer(hidden_2, [128, 10], [10])
			
	################# training #################
	trainEpochs = 10
	batchSize = 200
	last_acc = 0
	totalBachs = math.ceil(len(traData)/batchSize)	
	
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
				print("Train Epoch "+str(epoch+1)+": "+str(i+1)+" / "+str(totalBachs))
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
	
	
	
	
	
	
	