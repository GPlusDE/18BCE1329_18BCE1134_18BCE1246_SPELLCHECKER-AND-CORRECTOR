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
def correct(sentence):
    "This function returns the corrected sentence based on bigram probability."
    corrected = []
    cnt = 0
    indexes = []
   
    for i in sentence:

        if i.lower() not in unique_words:
            indexes.append(cnt)
            if len(get_candidates(i)) > 1:

                suggestion = get_candidates(i)
                prob = []

                for sug in suggestion:

                    if ((cnt != 0) and (cnt != len(sentence)-1)):
                    
                        p1 = cf_biag[sug.lower()].prob(sentence[cnt+1].lower())
                        p2 = cf_biag[corrected[len(corrected)-1].lower()].prob(sug.lower())
                        p = p1 * p2
                        prob.append(p)     
                    
                    
                    else:

                        if cnt == len(sentence)-1:
                            
                            p2 = cf_biag[corrected[len(corrected)-1].lower()].prob(sug.lower())
                            prob.append(p2)

                        elif cnt == 0:
                        
                            p1 = cf_biag[sug.lower()].prob(sentence[cnt+1].lower())
                            prob.append(p1)

                if len(suggestion[prob.index(max(prob))]) > 1:
                    corrected.append(suggestion[prob.index(max(prob))])
                else:
                    corrected.append(suggestion[prob.index(max(prob))])

            else:
                corrected.append(get_candidates(i)[0])

        else:
            corrected.append(i)

        cnt = cnt+1
    return corrected


print(correct(["this","whitr","cat"]))
assert(correct(["this","whitr","cat"]) == ['this','white','cat'])