f = open(r"stop-word-list.txt","r")

STOPWORDS = f.read()

STOPWORDS = STOPWORDS.split('\n')
