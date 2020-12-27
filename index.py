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
def parsing(sent):  
    """Parsing the sentence to corrected and original and storing in the dictionary."""
    loriginal = []
    lcorrected = []
    lcorr = []
    indexes = []
    cnt = 0
    
    for i in sent:
        if '|' in i:

            str1 = i.split('|')
            loriginal.append(str1[0])
            lcorrected.append(str1[1])
            indexes.append(cnt)
        
        else:
            loriginal.append(i)
            lcorrected.append(i)
        cnt = cnt+1
     
    dictionary = {'original': loriginal, 'corrected': lcorrected, 'indexes': indexes}
    
    return dictionary




def preprocessing():
    """Loading the data from 'abc.txt' and passing to parsing function to get parssed sentences. 
    Returning the whole dictionary as data."""
    data = []

    text_file = open("abc.txt", "r")
    lines = []
    for i in text_file:
        lines.append(i.strip())

    sentences = [nltk.word_tokenize(sent) for sent in lines]

    for sent in sentences:
        data.append(parsing(sent))
    
    return data

data = preprocessing()

print(data[2])
assert(data[2] == {
 'original': ['I', 'have', 'four', 'in', 'my', 'Family', 'Dad', 'Mum', 'and', 'siter', '.'],
 'corrected': ['I', 'have', 'four', 'in', 'my', 'Family', 'Dad', 'Mum', 'and', 'sister', '.'],
 'indexes': [9]
})

test = data[:100]
train = data[100:]