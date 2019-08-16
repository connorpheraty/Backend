import pandas as pd 
from collections import Counter

# Instantiate DataFrame from cleaned csv 
df = pd.read_csv('Final.csv')

def token_counts(string, search):
  """
  Function that counts the number of times a user search term is mentioned in a given tokenized list
  """
    counter = Counter(string.strip('[],"').split(','))
    count = []
    for key, val in counter.items():
        if key.strip(" '") in search:
            count.append(int(val))
    return sum(count)    

def trial_ranker(user_search):
  """
  Function that ranks each trial using the token_counts function
  """

  df = pd.read_csv('Final.csv')
  df['counts'] = df['tokens'].apply(lambda x: token_counts(x, user_search))
  
  # Sort dataframe by counts column descending from highest to lowest
  df_sorted = df.sort_values(by=['counts'], ascending=False)
  df_sorted = df_sorted.drop('counts', axis=1)

  # Return top 15 results
  df_sorted = df_sorted.head(15)

  return df_sorted

