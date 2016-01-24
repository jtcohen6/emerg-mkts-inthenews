import requests
import nltk
import pandas

"""
Class to split each sentence into individual words
Inspiration from: https://github.com/fjavieralba/basic_sentiment_analysis
"""

class Split_Sentences(object):

    def __init__(self):
    	nltk.download('punkt')
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        final_list = [[item.replace('.', '') for item in lst] for lst in tokenized_sentences]
        return final_list




"""
Open csv files, and create pandas dataframe with matchings between title and etf ticker symbol.
Goal is to use this with Blackrock API and get relevant information
Goal is to then visualize using Beaker/c3.js/d3.js
"""


if __name__ == '__main__':
	text = """To they four in love. 
	Settling you has separate supplied bed. Concluded resembled suspected his resources curiosity joy. 
	Led all cottage met enabled attempt through talking delight. Dare he feet my tell busy. 
	Considered imprudence of he friendship boisterous. 
	"""
	sentence_splitter = Split_Sentences()
	splitted_sentences = sentence_splitter.split(text)

	print(splitted_sentences)
