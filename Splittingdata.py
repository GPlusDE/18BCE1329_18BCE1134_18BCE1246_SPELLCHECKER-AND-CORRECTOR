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
def test_train_split():
    """Splitting the data to test - first 100 lines and remaining training lines."""
    test = data[:100]
    train = data[100:]

    train_corrected = [elem['corrected'] for elem in train]
    tokenizer = RegexpTokenizer(r'\w+')
    test_corrected = [elem['corrected'] for elem in test]
    test_original = [elem['original'] for elem in test]

    test_original = [tokenizer.tokenize(" ".join(elem)) for elem in test_original]
    test_corrected = [tokenizer.tokenize(" ".join(elem)) for elem in test_corrected]
    train_corrected = [tokenizer.tokenize(" ".join(elem)) for elem in train_corrected]
    
    return test_corrected, test_original, train_corrected

test_corrected, test_original, train_corrected = test_train_split()