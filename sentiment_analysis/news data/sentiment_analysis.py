#!usr/bin/python

import pandas as pd 
from vaderSentiment import vaderSentiment


#need to access pandas data frame (start and stop)
def read_articles(file):
	with open(file) as input_file:
		start = [item for item in data[data.columns[2]]]
		end = [item for item in data[data.columns[3]]]	
		temp = []
		container = list(input_file)
		for i,j in zip(start,end):
			temp.append(''.join(container[i:j]))
		return temp

def calculate_score(articles):
	df = pd.DataFrame(data[data.columns[1:5]])
	df["sent_scores"] = ""
	for i in range(len(articles):
		df["sent_scores"].loc(i) = vaderSentiment.sentiment(articles[i])
	return df
	
def main(csv_file,txt_file):
	data = pd.read_csv(csv_file)
	articles = read_articles(txt_file)
	df = calculate_score(articles)
	df.to_csv(csv_file.split('.',2)[0] + "_sent_scores.csv")

if __name__ == "__main__":
	main("ftimes.csv","ftimes21494.txt")
	main("forbes.csv","forbes1220.ansi.txt")