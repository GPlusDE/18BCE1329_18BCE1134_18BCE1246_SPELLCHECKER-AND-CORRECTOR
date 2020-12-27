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
from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:

    print(spell.correction(word))

    print(spell.candidates(word))