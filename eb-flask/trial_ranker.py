import pandas as pd 
from collections import Counter

df = pd.read_csv('Final.csv')

def token_counts(string, search):
    counter = Counter(string.strip('[],"').split(','))
    count = []
    for key, val in counter.items():
        if key.strip(" '") in search:
            count.append(int(val))
    return sum(count)    

def trial_ranker(user_search):

  df = pd.read_csv('Final.csv')
  print(user_search)

  df['counts'] = df['tokens'].apply(lambda x: token_counts(x, user_search))
  

  df_sorted = df.sort_values(by=['counts'], ascending=False)
  print(df_sorted['counts'])
  print(df_sorted['counts'].value_counts())

  df_sorted = df_sorted.drop('counts', axis=1)


  df_sorted = df_sorted.head(15)

  return df_sorted

