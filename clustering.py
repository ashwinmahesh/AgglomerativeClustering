import nltk
import time
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 

from XMLParser import XMLParse
from TFIDF import TFIDF

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
  startTime = time.time()

  print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

  print("Extracting data from XML Document...")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm")
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

  print("Computing TF, IDF, and TFIDF...")
  computedTFIDF = TFIDF(values, uniqueWords)
  idfTime = round(time.time() - startTime - extractionTime - removingTime - uniqueWordsTime, 3)
  print("Time: " + str(idfTime) + " seconds")

  print("Computing Cosine Similarity...")
  computedTFIDF.calculateCosineSimilarity()
  computedTFIDF.printVal('sim', 19)
  cosineSimTime = round(time.time() - startTime - extractionTime - removingTime - uniqueWordsTime - idfTime, 3)
  print("Time: " + str(cosineSimTime) + " seconds")


  print('PROGRAM HAS TERMINATED EXECUTION')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")

    # printVal=''
    # for i in range(0, len(tf)):
    #   if tf[i]>0:
    #     printVal+=(uniqueWords[i]+': '+str(i) + '\t')
    # print(printVal)
    # print("IDF:", idf)
 
