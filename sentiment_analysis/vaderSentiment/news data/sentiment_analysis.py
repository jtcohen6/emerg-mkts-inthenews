#!usr/bin/python

import pandas as pd 

# create data frame of csv files and extract art_start
data = pd.read_csv('ftimes.csv')

#need to access pandas data frame (start and stop)
def read_articles(file):
	with open(file) as input_file:
		start = [item for item in data[data.columns[2]]]
		end = [item for item in data[data.columns[3]]]	
		temp = []
		container = list(input_file)
		for i,j in zip(start,end):
			temp.append(''.join(container[i:j]))





read_articles('ftimes21494.txt')
# read_articles('forbes1220.ansi.txt')
