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

def findWordIndex(uniqueWordList, word):
  try:
    wordIndex = uniqueWordList.index(word)
    return wordIndex
  except ValueError:
    return -1

#Takes in a stemmed and stopped document, along the list of all the words in the corpus, and returns the TF Vector
def calculateTermFrequency(document, uniqueWordList):
  tfOutput=[0] * len(uniqueWordList)
  docWords = document.getField('BODY').split()
  for word in docWords:
    index = findWordIndex(uniqueWordList, word)
    if index != -1:
      tfOutput[index]+=1
  return tfOutput

def calculateIDF()

if __name__ == '__main__':
  print("\nAgglomerative Clustering by Ashwin Mahesh\n")
  print("Extracting data from XML Document...")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm")
  print("Removing stopwords and stemming...")
  for i in range(len(values)-1, -1, -1):
    if values[i].hasField('BODY'):
      values[i].setField('BODY',removeStopwords(values[i].getField("BODY")))
    else:
      del values[i]
  
  print("Creating list of all unique words in corpus...")
  uniqueWords = getUniqueWords(values)

  for i in range(0, 5):
    print('Iteration: '+str(i))
    tf = calculateTermFrequency(values[i], uniqueWords)
    printVal=''
    for i in range(0, len(tf)):
      if tf[i]>0:
        printVal+=(uniqueWords[i]+': '+str(i) + '\t')
    print(printVal)
 
