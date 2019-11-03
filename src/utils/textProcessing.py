import pandas as pd 
import numpy as np
import re 

from stopWords import STOPWORDS
from textHelper import indexDataFrame

df = pd.read_csv('input.csv', index_col=0)

# Remove NaN values from state column
df['state'] = df['state'].replace({np.nan: 'None'})

# Remove duplicate studies from dataframe
df['is_duplicate'] = df.duplicated(keep='first')
df = df[(df['is_duplicate'] == False)]
# Drop duplicates row
df = df.drop(['is_duplicate'], axis=1)


# Create tokens column from selected study categories
df['tokens'] = df['brief_summary'] + df['condition'] + df['city'] + df['country'] + df['official_title'] + df['state']
df['tokens'] = [re.sub(r'[^\w\s]','',i) for i in df['tokens']] 
df['tokens'] = [i.lower().split() for i in df['tokens']]

# Index token column
df = indexDataFrame(df, 'tokens', STOPWORDS)

df.to_csv('output.csv', index=False)
