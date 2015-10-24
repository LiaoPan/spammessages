#!/usr/bin/env python
#-*-coding:utf-8-*-
#ex for scikit-learn
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import jieba

# iris = datasets.load_iris()
# gnb = GaussianNB()
# y_pred = gnb.fit(iris.data,iris.target).predict(iris.data)  #iris.data is numpy.ndarray.
# print("Number of mislabeld points out of a total %d points:%d"%(iris.data.shape[0],(iris.target != y_pred).sum()))

#=======================================================
#load  train data
train_file = pd.read_table("train_sample.txt",names = ["ID","Value","String"])
print "load's file length:",len(train_file)
#load test data
test_file = pd.read_table("test.txt",names = ["ID","String"])
# print test_file.head()
# print np.array(test_file["String"])
#convert to np.ndarray
print train_file.tail()

#==========================================================
#jieba participle
#parallel
jieba.enable_parallel(1) #start:the paralleled num of processes;but one is better.
jieba.set_dictionary("dict_for_jieba.txt") #set dictionary dir

trainData = []
for s in train_file["String"]:
    trainData.append("/".join(jieba.cut(s)))

print len(trainData)
print trainData[0]


jieba.disable_parallel() #turn off processes

#============================================================
#TF-IDF :Extract features.



#train_data = np.array(trainData["String"],dtype=np.float64)
train_target = np.array(train_file["Value"],dtype=np.float64)
#print train_target
# print train_data[1]
# print train_target[1]
#
# test_data = np.array(test_file["String"],dtype=np.float64)
# # print test_data[0]
# #=======================================================
# #train the data
# gnb = GaussianNB()
# y_pred = gnb.fit(train_data,train_target).predict(test_data)
# print y_pred