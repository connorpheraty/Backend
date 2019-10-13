import pandas as pd 
import re 

from stopWords import STOPWORDS
from indexHelper import indexDataFrame

df = pd.read_csv('Final.csv')

df['tokens'] = df['brief_summary'] + df['condition'] + df['city'] + df['country'] + df['official_title'] + df['state']


df['tokens'] = [re.sub(r'[^\w\s]','',i) for i in df['tokens']] 
df['tokens'] = [i.lower().split() for i in df['tokens']]

df = indexDataFrame(df, 'tokens', STOPWORDS)

df = df.drop(columns=['Probability Completed', 'Unnamed: 0'])

df.to_csv('indexed_csv.csv')