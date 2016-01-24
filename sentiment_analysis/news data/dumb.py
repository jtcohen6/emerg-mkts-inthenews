import pandas as pd 

data = pd.read_csv('ftimes.csv')
df = pd.DataFrame(data[data.columns[1:5]])
df["sent_scores"] = ""

x = 0
for i in range(len(df["sent_scores"])):
	df['sent_scores'] = [data.index.get_loc(i) for i in data.index]