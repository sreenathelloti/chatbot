# All imports here

import nltk
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re


import SpellCorrection

# Functions Defined
vect = TfidfVectorizer()
# Function to create list

def columnstoList(data):
   Ques=list(data.iloc[:,0])
   Resp=list(data.iloc[:,1])
   return Ques,Resp


def tokenization_spellcheck(sample_list):
   corpus = []
   for i in range(len(sample_list)):
         review = re.sub('[^a-zA-Z1-9]', ' ', sample_list[i])
         review = review.lower()
         review = review.split()
         #Spell Correction
         for k in range(len(review)):
            review[k]=SpellCorrection.correction(review[k])
         #Stemming And Stopwords   
         ps = PorterStemmer()
         review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
         
         review = ' '.join(review)
         corpus.append(review)
   return corpus

# Function to create tfidfvectorizer
def createTfidfVectorizer(queslist):
    qmatrix = vect.fit_transform(queslist).toarray()
    return qmatrix



def createTfidfVectorizer_Instance(queslist):
    rmatrix = vect.transform(queslist).toarray()
    return rmatrix


    
   


