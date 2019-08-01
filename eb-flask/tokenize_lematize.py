# Spacy
import spacy
nlp = spacy.load("en_core_web_sm")

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess

# stopword
import nltk; nltk.download('stopwords')

# NLTK Stop words
from nltk.corpus import stopwords


def lemmatization(text, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []

    doc = nlp(" ".join(text))
    
    texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    
    return texts_out


def tokenize_lemmatize(string):

    tokens = gensim.utils.simple_preprocess(str(string), deacc=True)

    stop_words = stopwords.words('english')
    stop_words.extend(['disease', 'symptom'])

    tokens = [word for word in tokens if word not in stop_words]

    tokens_lemmatized = lemmatization(tokens, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

    return tokens_lemmatized






