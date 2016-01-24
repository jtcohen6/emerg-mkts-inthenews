#!usr/bin/python

import pandas as pd 
import nltk
import sentlex
import sentlex.sentanalysis

# Load Lexicon
SWN = sentlex.SWN3Lexicon()



def main(csv_file, txt_file, limit):
	with open(txt_file) as input_file:
		data = pd.read_csv(csv_file)
		data = data.head(limit)
		df = pd.DataFrame(data[data.columns[1:5]])
		df["positive_sentiment"] = ""
		df["negative_sentiment"] = ""
		start = [item for item in data[data.columns[2]]]
		end = [item for item in data[data.columns[3]]]	
		articles = []
		container = list(input_file)
		for i,j in zip(start,end):
			articles.append(''.join(container[i:j]))
		for i in range(limit):
			classifier = sentlex.sentanalysis.BasicDocSentiScore()
			sentiment = classifier.classify_document(articles[i], tagged=False, L=SWN, a=True,
				v=True, n=False, r=False, negation=False, verbose=False)
			df.loc[i, 'positive_sentiment'] = sentiment[0]
			df.loc[i, 'negative_sentiment'] = sentiment[1]
	# print(df)
	df.to_csv(csv_file.split('.',2)[0] + "_sent_classifier_scores.csv")

if __name__ == "__main__":
	main("ftimes.csv","ftimes21494.txt")
	main("forbes.csv","forbes1220.ansi.txt", 50)


