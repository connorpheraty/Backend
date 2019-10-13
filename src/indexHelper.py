from collections import Counter
import math
import re

def indexDataFrame(df, token_array, stopwords):
    counter_lst = []
    for i in df[token_array]:
        temp_lst = []
        for j in i:
            if j not in stopwords:
                temp_lst.append(j)
        temp_lst = Counter(temp_lst)
        temp_lst = dict(temp_lst)
        counter_lst.append(temp_lst)
    df['term_freq'] = counter_lst
    return df

def tokenizer(string):

    tokenized_lst = string.split()
    tokenized_lst = [re.sub(r'[^\w\s]','',i) for i in tokenized_lst]
    tokenized_lst = [i.lower() for i in tokenized_lst]

    return tokenized_lst



def search_freq(tokenized_search_terms, df, index=None, counter=0 ):
    """Returns the number of times a search term is mentioned per document in a corpus of documents"""

    for j in tokenized_search_terms:

        if not index:
            index = {}
        search_term = j
        
        for i in df['term_freq']:
            if search_term in i:
                counter +=1
        index.update({j:counter})
        counter = 0
    return index

def score_docs(index, df, score=0):
    """Returns a tf-idf score for a given search"""
    
    N = len(df)

    zero_lst = [i*0 for i in (range(N))]
    
    for i, j in index.items():
        val = math.log(N/j)
        temp_lst = []
        for k in df['term_freq']:
            if i in k:
                score += val
            else:
                score = 0
            temp_lst.append(score)
            score = 0
        
        zero_lst = [x + y for x, y in zip(zero_lst, temp_lst)]
        df['score'] = zero_lst

    df = df.sort_values('score', ascending=False)

    df = df.head(20)

    return df