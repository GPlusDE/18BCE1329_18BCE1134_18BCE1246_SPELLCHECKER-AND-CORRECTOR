#Importing all required libraries for this task.
import nltk
nltk.download('punkt')
from nltk.util import ngrams
from nltk.metrics.distance import edit_distance
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
from itertools import chain
import json
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import *
from nltk.corpus import wordnet as wn
import time
from tqdm import tqdm
from difflib import SequenceMatcher
lemmatizer = WordNetLemmatizer()
def unigram(words):
    """This function returns a unigram frequency for a given word."""
    doc = []
    words = words.lower()
    for i in train_corrected:
        doc.append(" ".join(i).lower())

    doc = " ".join(doc)    
    doc = nltk.word_tokenize(doc)

    unig_freq = nltk.FreqDist(doc)

    tnum_unig = sum(unig_freq.values())
    
    return unig_freq[words], tnum_unig

e, f = unigram('me')
print("unigram('me')==", e)
def bigram(words):
    """This function returns a bigram frequency for a given words."""
    doc = []

    words = words.split(" ")
    words[0] = words[0].lower()
    words[1] = words[1].lower()
    words = tuple(words)
    
    for i in train_corrected:
        doc.append(" ".join(i))
        
    doc = " ".join(doc)    
    doc = doc.lower()

    tokens = nltk.wordpunct_tokenize(doc)
    bigrams=nltk.collocations.BigramCollocationFinder.from_words(tokens)
    biag_freq = dict(bigrams.ngram_fd)

    tnum_bg = sum(biag_freq.values())

    try:
        return biag_freq[words], tnum_bg
    except KeyError:
        return 0, 0
    
    
a, b = bigram("my mother")
print("bigram('my mother')==", a)
c, d = bigram("you did")
print("bigram('you did')==", c)