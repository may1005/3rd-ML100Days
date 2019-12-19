#-*- coding: utf-8 -*-　
import numpy as np 
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import csv
import math
from pandas import DataFrame
from time import time

if __name__ == '__main__':		
	homefolder = "D:\\AI_Train\\Kaggle\\DigitRecognizer\\"
	modelFile = homefolder+'\\Model\\model.ckpt.meta'
	predictFile = homefolder+'Output\\PredResult.csv'
	
	################# read test data #################
	df_test = pd.read_csv("test.csv")
	testData = np.array(df_test.values.tolist())
	
	with tf.Session() as sess:	
		################# read model #################		
		saver = tf.train.import_meta_graph(modelFile)		
		saver.restore(sess, tf.train.latest_checkpoint(homefolder+'\\Model\\'))
		
		graph = tf.get_default_graph()
		x = graph.get_tensor_by_name("x:0")	
		output_layer = graph.get_tensor_by_name("output_layer:0")		
		
		################# predict #################
		pred_result = sess.run(output_layer, feed_dict={x: testData})	
		final_result = sess.run(tf.argmax(pred_result, 1))
		
		################# write the results of prediction into file #################	
		f = open(predictFile,"w")			
		title = "ImageId,Label\n"
		f.write(title)		
		for i in range(0, len(final_result)):
			result = str(i+1)+","+str(final_result[i])+"\n"
			f.write(result)
		f.close()
		
		
		