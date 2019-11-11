import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from XMLParser import XMLParse
import numpy as np
import time
import math

class TFIDF:
  def __init__(self, allTFs, docCount):
    self.docCount = docCount
    self.allTFs = np.array(allTFs)
    self.idf = np.zeros(len(self.allTFs[0]))
    self.tfidf=[]

    self.calculateIDF()
    self.calculateTFIDF()
  
  #Calculates the IDF score based on inputted TF
  def calculateIDF(self):
    counts = np.zeros(len(self.allTFs[0]))
    for tf in self.allTFs:
      containedIndexes = np.where(tf>0)
      for index in containedIndexes:
        counts[index]+=1
    
    for i in range(0, len(counts)):
      self.idf[i] = math.log(self.docCount / (counts[i]), 2)

  #Calculates TFIDF Based on Inputted TF and IDF
  def calculateTFIDF(self):
    for i in range(0, self.docCount):
      self.tfidf.append(np.multiply(self.allTFs[i], self.idf))

  #Prints the value in any of the three fields
  def printVal(self, valName, index=0):
    np.set_printoptions(threshold=np.inf)
    if(valName == 'tfidf'):
      print(self.tfidf[index])
    elif valName == 'tf':
      print(self.allTFs[index])
    elif valName == 'idf':
      print(self.idf)


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

#Takes in a stemmed and stopped document, along the list of all the words in the corpus, and returns the TF Vector. Calculates a running IDF
def calculateTermFrequency(document, uniqueWordList):
  tfOutput=[0] * len(uniqueWordList)
  docWords = document.getField('BODY').split()
  for word in docWords:
    index = findWordIndex(uniqueWordList, word)
    if index != -1:
      tfOutput[index]+=1
  return tfOutput


if __name__ == '__main__':
  startTime = time.time()

  print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

  print("Extracting data from XML Document...")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm", 100, True)
  print("Number of Documents: "+str(len(values)))
  extractionTime = round(time.time() - startTime, 3)
  print("Time: " + str(extractionTime) + " seconds")

  print("Removing stopwords and stemming...")
  for i in range(len(values)-1, -1, -1):
    if values[i].hasField('BODY'):
      values[i].setField('BODY',removeStopwords(values[i].getField("BODY")))
    else:
      del values[i]
  removingTime = round(time.time() - startTime - extractionTime, 3)
  print("Time: " + str(removingTime) + " seconds")

  print("Creating list of all unique words in corpus...")
  uniqueWords = getUniqueWords(values)
  uniqueWordsTime = round(time.time() - startTime - extractionTime - removingTime, 3)
  print("Time: " + str(uniqueWordsTime) + " seconds")


  print("Calculating all term frequencies...")
  TFs=[]
  for i in range(0, len(values)):
    TFs.append(calculateTermFrequency(values[i], uniqueWords))
  tfTime = round(time.time() - startTime - extractionTime - removingTime - uniqueWordsTime, 3)
  print("Time: " + str(tfTime) + " seconds")

  print("Creating TFIDF class and computing IDF...")
  computedTFIDF = TFIDF(TFs, len(values))
  # computedTFIDF.printVal('tfidf', 0)
  idfTime = round(time.time() - startTime - extractionTime - removingTime - uniqueWordsTime - tfTime, 3)
  print("Time: " + str(idfTime) + " seconds")


  print('PROGRAM HAS TERMINATED EXECUTION')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")

    # printVal=''
    # for i in range(0, len(tf)):
    #   if tf[i]>0:
    #     printVal+=(uniqueWords[i]+': '+str(i) + '\t')
    # print(printVal)
    # print("IDF:", idf)
 
