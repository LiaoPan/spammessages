#coding:utf-8
#author:L.P
#time:201510222012
import pandas as pd
import  numpy as np
import re
import jieba
import time

t1 = time.time()

#=====================First,load  text file and convert them into terms vectors.=========================#
train_file = pd.read_table("train.txt",names = ["ID","Value","String"])
#print train_file["String"]

#parallel
jieba.enable_parallel(1) #start:the paralleled num of processes;but one is better.
jieba.set_dictionary("dict_for_jieba.txt") #set dictionary dir

trainData = []
for s in train_file["String"]:
    trainData.append("/".join(jieba.cut(s)))

print len(trainData)
print trainData
jieba.disable_parallel() #turn off processes


#try cloud9



t2 = time.time()

print "The program cost:%ss"%(t2-t1)