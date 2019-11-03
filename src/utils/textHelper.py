from collections import Counter

def indexDataFrame(df, token_array, stopwords):
    """Indexes an array of tokens"""
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
