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

import text_processor as txt_p
import tfidf 

print("hi")
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
# values to empty list
for col in file:
    talk_IDs.append(col['talk_id'])
    # speakersX.append(col['all_speakers'])
    # topicsX.append(col['topics'])
    # descriptionsX.append(col['description'])
    transcriptsX.append(col['transcript'])

# for cleaned data
speakers = []
topics = []
descriptions = []
transcripts = []

# clean speakers and topics columns
# txt_p.clean_column(speakersX, speakers)
# txt_p.clean_column(topicsX, topics)

print("processing transcripts...")
# process transcript documents
for transcript in transcriptsX:
  transcripts.append(txt_p.process(transcript))
print("finished processing...")

size = len(transcriptsX) / 20
test_transcripts = transcripts[0:size]
test_talk_IDs = talk_IDs[0:size]

print("zipping talk_ids to transcripts")
# consolidate talk_IDs and processed transcripts into a dict
processed_transcripts = dict(zip(test_talk_IDs, test_transcripts))
json_processed_transcripts = json.dumps(processed_transcripts)
jsonFile = open("processed_transcripts.txt", "w")
jsonFile.write(json_processed_transcripts)
jsonFile.close()

# printing lists
# print('Speakers:', speakers[10])
# print('\nTopics:', topics[10])
# print('\nDescriptions:', descriptions[10])
# print('\nTranscripts', transcripts[10])

# get user input
# input = input("Enter search parameters:\n")