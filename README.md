# 18BCE1329_18BCE1134_18BCE1246_SPELLCHECKER-AND-CORRECTOR
# A Project submitted to Dr.Radhikaselvamani
# by 18BCE1329-Jitendra sai 18BCE1134-Dheeraj kannan 18BCE1246-Saandeep

Introduction:

Spell Check is a process of detecting and sometimes providing suggestions for misspelledly spelled words in a text.
In computing, Spell Checker is an application program that flags words in a document that may not be spelled correctly.
Spell Checker may be stand- alone capable of operating on a block a text such as word-processor, electronic dictionary.
A basic spell checker carries out the following processes:
It scans the text and extracts the words contained in it.
It then compares each word with a known list of correctly spelled words.
An additional step is a language-dependent algorithm for handling morphology.
Spell check and correction has been a key part of natural language processing which motivated us to take this topic.
This topic is used everywhere from normal documents to social networking websites and search engines this concept is used so it made this topic very important for us to take.
we are exploring Spell Checking, a very important task in any serious NLP pipeline that needs to deal with noisy, misspelled data that has been generatedin the wild.


Process:

We had developed a  spellchecking system and an evaluation of its performance.We used Python for completing this. 
In the first part we created a  parser that can read all the lines of the file abc.txt and print out for each line the original (misspelled) text, the corrected text and the indexes of any changes. The indexes refers to the index of the words in the sentence.
In the second part we  Calculated the frequency (number of occurrences), ignoring case, of all words and bigrams (sequences of two words) from the corrected training sentences.
In the third part we used Edit distance is a method that calculates how similar two strings are to one another by counting the minimum number of operations required to transform one string into the other.
In fourth part we wrote a function that takes a (misspelled) sentence and returns the corrected version of that sentence.
The system should scan the sentence for words that are not in the dictionary (set of unique words in the training set) and for each word that is not in the dictionary choose a word in the dictionary that has minimal edit distance and has the highest bigram probability. In fifth part  by Using the test corpus we evaluated the accuracy of our method, how many words from your system's output match the corrected sentence.
Finally Using the test corpus we evaluated the accuracy of our method, i.e., how many words from our system's output match the corrected sentence (you should count words that are already spelled correctly and not changed by the system).
