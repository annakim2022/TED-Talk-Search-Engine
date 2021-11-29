import csv
import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
nltk.download("punkt")


# open the file in read mode
filename = open('ted_talks_en.csv', 'r')
# creating dictreader object
file = csv.DictReader(filename)

# clean columns
disallowed = "}{][]:'1234567890"
def clean_column(list, cleaned_list):
  for str in list:
    for char in disallowed:
      str = str.replace(char,"")
    cleaned_list.append(str)

# process text: lower case, remove punctuations, tokenize, and stem (no need to remove stopwords)
def process(document):
  # 1. case folding -> lower case
  document = document.lower()
  #2. remove punctuations
  document = "".join([char for char in document if char not in string.punctuation])
  #3. tokenization
  tokens = word_tokenize(document)
  #4. stemming
  stemmed_tokens = [porter.stem(word) for word in tokens]
  return stemmed_tokens

# calculate cosine similarity between two vectors
import numpy as np
def cosine_similarity(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    return np.dot(vector1,vector2) / (np.sqrt(np.sum(vector1**2)) * np.sqrt(np.sum(vector2**2)))