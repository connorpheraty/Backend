import pandas as pd

df = pd.read_csv('output.csv', index_col=0)

def age_parser(df):
    age_lst = []
    for i in df['eligibility']:
        samp = i.split("\n")
        temp_lst = []
        for j  in samp:
            if j[-5:] == "Years":
                temp_lst.append(int(j[:2]))
        if len(temp_lst) < 1:
            temp_lst.append(None)
        if len(temp_lst) < 2:
            temp_lst.append(None)
        age_lst.append(temp_lst)

    return age_lst

def age_buckets(df, age_lst):

    min_age = []
    max_age = []

    for i in age_lst:
        min_age.append(i[0])
        max_age.append(i[1])

    df['min_age'] = min_age
    df['max_age'] = max_age

    return df

age_lst = age_parser(df)
df = age_buckets(df, age_lst) 

df.to_csv('output.csv', index=False)

