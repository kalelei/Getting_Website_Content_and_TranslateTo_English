import string
import requests
from bs4 import BeautifulSoup
from langdetect import detect
from nltk.translate import Alignment,AlignedSent
from googletrans import Translator
import lxml


translator = Translator()


url = 'https://www.hurriyet.com.tr/'

response = requests.get(url)
#print(response.content)
#print(response.text)
soup = BeautifulSoup(response.content, 'html.parser') # makes response.content code more simple



words = soup.find_all('p')  #finding all the <p> tags which are in the soup object
for word in words:                #for direct paragraphs  
  print('Mother tounge is',translator.detect(word.text).lang, word.text,'-------->', translator.translate(word.text, dest='en').text)




"""for word in words:                  #get the paragraph and split into words
  word = word.text.split()
  for w in word:
    print('Mother tounge is',translator.detect(w).lang, w,'-------->', translator.translate(w, dest='en').text)"""