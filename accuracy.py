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
start_time = time.time()
def accuracy(acsnitual_sent, sent_pred):
    """This is based on word to word accuracy calculation. Compares each word with the actual word and calculate accuracy"""
    actual = actual_sent
    predict = correct(sent_pred)

    if len(actual) == 0 and len(predict)==0:
        accuracy = 1.0
    else:

        accuracy = len(set(predict) & set(actual))/len(set(actual))
    
    return accuracy

acc = []
for i in tqdm(range(len(test_corrected))):
    acc.append(accuracy(test_corrected[i], test_original[i]))
    
    
print("*****************EVALUATION*******************")
print("Average Accuracy of words in each sentence: ", round(sum(acc)/len(acc)*100, 4), "%")
print(acc.count(1), "out of 100 sentences predicted correctly without any error.")
elapsed_time = time.time() - start_time
print("Elapsed Time is: ", elapsed_time)