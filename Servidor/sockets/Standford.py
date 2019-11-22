import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
# Passing the string text into word toke
data = pd.read_csv(name_data, sep=';',encoding ='latin1')
token = word_tokenize(data['Tweet content'])
fdist = FreqDist(token)