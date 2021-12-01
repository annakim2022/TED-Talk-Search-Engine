import csv
import nltk
import string
import json
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

# creating empty lists for raw data
talk_IDs = []
speakersX = []
topicsX = []
descriptionsX = []
transcriptsX = [] 
 
# iterating over each row and append
#values to empty list
for col in file:
   talk_IDs.append(col['talk_id'])
   speakersX.append(col['all_speakers'])
   topicsX.append(col['topics'])
   descriptionsX.append(col['description'])
   transcriptsX.append(col['transcript'])

# for cleaned data
speakers = []
topics = []
descriptions = []
transcripts = []

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

# clean speakers and topics columns
clean_column(speakersX, speakers)
clean_column(topicsX, topics)

# process transcript documents
for transcript in transcriptsX:
  transcripts.append(process(transcript))

# make dict {TedTalk: Transcript}
processed_transcripts = dict(zip(talk_IDs, transcripts))

# dump dict into json 
json_dict = json.dumps(processed_transcripts)
jsonFile = open("processed_transcripts.txt", "w")
jsonFile.write(json_dict)
jsonFile.close()



