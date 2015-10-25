#coding:utf-8
#author:L.P 
import pandas as pd

file = pd.read_table("test.txt",names=["ID","string"])
for s in file["string"]:
	file["string"] = 1
	
sub = pd.write_csv("submit.csv",sep=",")