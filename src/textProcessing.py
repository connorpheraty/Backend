import pandas as pd 
import re 
#import nltk
#from nltk.stem import PorterStemmer
#nltk.download('punkt')

from stopWords import STOPWORDS
from indexHelper import indexDataFrame

ps = PorterStemmer()

df = pd.read_csv('Final.csv')

df['tokens'] = df['brief_summary'] + df['condition'] + df['city'] + df['country'] + df['official_title'] + df['state']

df['tokens'] = [re.sub(r'[^\w\s]','',i) for i in df['tokens']] 

df['tokens'] = [i.lower().split() for i in df['tokens']]

"""
gods_lst = []
for i in df['tokens']:
    emt_lst = []
    for j in i:
        k = ps.stem(j)
        emt_lst.append(j)
    gods_lst.append(emt_lst)

df['tokens'] = gods_lst
"""


df = indexDataFrame(df, 'tokens', STOPWORDS)

df = df.drop(columns=['Probability Completed', 'Unnamed: 0'])

df.to_csv('indexed_csv.csv')