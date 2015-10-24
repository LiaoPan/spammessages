#coding:utf-8
#author:L.P
import pandas as pd
import numpy as np
import jieba
from tgrocery import Grocery
#=======================================================
#load  train data
train_file = pd.read_table("train_sample.txt",names = ["ID","Value","String"])
print "load's file length:",len(train_file)
#load test data
test_file = pd.read_table("test.txt",names = ["ID","String"])

#print train_file["Value"]  # it is a pandas.series
#train_file must convert to list.
train_value = train_file["Value"].tolist()
#print train_value[1]
train_string = train_file["String"].tolist()
train_src = zip(train_value,train_string)
print train_src[0]

#test file
test_src = test_file["String"].tolist()



#tgrocery classify
grocery =Grocery('sample')
grocery.train(train_src)
grocery.save()
new_grocery = Grocery('sample')
new_grocery.load()

print new_grocery.predict("以上比赛规则由江苏科技大学教职工摄影协会负责解释")
