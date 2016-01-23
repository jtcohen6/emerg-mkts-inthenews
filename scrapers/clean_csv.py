import pandas as pd
import os


class Tickers(object):
	def __init__(self):
    	nltk.download('punkt')
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        final_list = [[item.replace('.', '') for item in lst] for lst in tokenized_sentences]
        return final_list


def clean_csv(csv):
	df = pd.read_csv(csv)
	df = pd.DataFrame(df[df.columns[0]].str.split('(').tolist(), columns = ['title', 'ticker'])
	df[df.columns[1]] = df[df.columns[1]].str.replace(')', '')
	temp_string = csv.split('/',2)
	output = temp_string[2].split('.',2)
	df.to_csv('data/csv_files/'+output[0]+'_clean.csv')



def clean_folder(folder):
	for subdir, dirs, files in os.walk(folder):
		for file in files:
			clean_csv(os.path.join(subdir, file))


clean_folder('data/csv_files')
