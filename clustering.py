import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from XMLParser import XMLParse

#Checks if the inputted string is a number, special in that commas do not make it not a number
def isNumber(string):
  for char in string:
    ascChar = ord(char)
    if not (ascChar >=48 and ascChar<=57) and char!='.' and char!=',':
      return False
  return True

#Uses NLTK To Porter Stem and Remove Stopwords
def removeStopwords(text):
  porterStemmer = PorterStemmer()
  stopWords = set(stopwords.words('english'))
  tokenedText = word_tokenize(text)
  newBody=''
  for word in tokenedText:
    if word not in stopWords:
      newBody+=porterStemmer.stem(word)
      newBody+=' '
  return newBody  

#Returns an ordered list of all the unique words in the corpus
def getUniqueWords(documents):
  output = []
  for document in documents:
    words = document.getField("BODY").split()
    for word in words:
      if isNumber(word) == False and word not in output:
        output.append(word)
  output.sort()
  return output

if __name__ == '__main__':
  print("Agglomerative Clustering")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm")
  for i in range(len(values)-1, -1, -1):
    if values[i].hasField('BODY'):
      values[i].setField('BODY',removeStopwords(values[i].getField("BODY")))
    else:
      del values[i]
    
  uniqueWords = getUniqueWords(values)
  print(uniqueWords)
  #for i in range(0, 5):
  #  print(i)
  #  print(values[i]["BODY"])

