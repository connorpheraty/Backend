import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess


# Words to be removed before ranking search
stop_words = ['i','me','my','myself','we','our','ours','ourselves','you',
              "you're","you've","you'll","you'd",'your','yours','yourself',
              'yourselves','he','him','his','himself','she',"she's",'her',
              'hers','herself','it',"it's",'its','itself','they','them','their',
              'theirs','themselves','what','which','who','whom','this','that',
              "that'll",'these','those','am','is','are','was','were','be','been',
              'being','have','has','had','having','do','does','did','doing','an',
              'the','and','but','if','or','because','as','while','of','at','by',
              'for','with','about','against','between','into','through','during',
              'before','after','above','below','to','from','up','down','in','out',
              'on','off','over','under','again','further','then','once','here','there',
              'when','where','why','how','all','any','both','each','few','more','most',
              'other','some','such','no','nor','not','only','own','same','so','than',
              'too','very','s','t','can','will','just','don',"don't",'should',"should've",
              'now','d','ll','m','o','re','ve','y','ain','aren',"aren't",'couldn',"couldn't",
              'didn',"didn't",'doesn',"doesn't",'hadn',"hadn't",'hasn',"hasn't",'haven',
              "haven't",'isn',"isn't",'ma','mightn',"mightn't",'mustn',"mustn't",'needn',
              "needn't",'shan',"shan't",'shouldn',"shouldn't",'wasn',"wasn't",'weren',"weren't",
              'won',"won't",'wouldn',"wouldn't",'disease','symptom','new','onset','prevalence','general',
              'practices','trial','patients','missing','phase','effectiveness','compare','study','safety']

def lemmatization(text, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    print(text)
    doc = " ".join(text)
    print(doc)
    
    texts_out.append([token.lemma_ for token in doc])
    
    return texts_out


def tokenize_lemmatize(string, stop_words=stop_words):
  """
  Tokenizes input string and removes stopwords
  """

    tokens = gensim.utils.simple_preprocess(str(string), deacc=True)

    tokens = [word for word in tokens if word not in stop_words]

    #tokens_lemmatized = lemmatization(tokens, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

    return tokens




