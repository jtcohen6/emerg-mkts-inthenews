#!usr/bin/python

import pandas as pd 
from vaderSentiment import vaderSentiment
import random


def random_sample(df_size, limit):
	random.seed(100)
	return random.sample(xrange(df_size), limit)

#need to access pandas data frame (start and stop)
def main(csv_file, txt_file, amount, name):
	with open(txt_file) as input_file:
		data = pd.read_csv(csv_file)
		rand_choices = random_sample(len(data), amount)
		new_df = data.loc[[i for i in rand_choices]]
		df = pd.DataFrame(new_df[new_df.columns[1:5]])
		df["vader_score_neg"] = ""
		df["vader_score_neu"] = ""
		df["vader_score_pos"] = ""
		df["vader_score_compound"] = ""
		start = [item for item in data[data.columns[2]]]
		end = [item for item in data[data.columns[3]]]	
		articles = []
		container = list(input_file)
		for i,j in zip(start,end):
			articles.append(''.join(container[i:j]))
		for i in df.index.values:
			df.loc[i, 'vader_score_neg'] = vaderSentiment.sentiment(articles[i])['neg']
			df.loc[i, 'vader_score_neu'] = vaderSentiment.sentiment(articles[i])['neu']
			df.loc[i, 'vader_score_pos'] = vaderSentiment.sentiment(articles[i])['pos']
			df.loc[i, 'vader_score_compound'] = vaderSentiment.sentiment(articles[i])['compound']
		df.to_csv(name+'_sentiment.csv')

if __name__ == "__main__":
	main("ftimes.csv","ftimes21494.txt", 100, "random_ftimes")
	main("forbes.csv","forbes1220.ansi.txt", 100, "random_forbes" )