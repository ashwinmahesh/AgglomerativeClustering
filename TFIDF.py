import math
import numpy as np
import time

class TFIDF:
  def __init__(self, documents, uniqueWordList):
    self.docCount = len(documents)
    self.documents = documents
    self.uniqueWordList = uniqueWordList
    self.allTFs = np.zeros((self.docCount, len(uniqueWordList)))
    self.idf = np.zeros(len(self.allTFs[0]))
    self.tfidf = np.zeros((self.docCount, len(uniqueWordList)))
    self.similarityMatrix = np.zeros((self.docCount, self.docCount))
    self.calculateTF().calculateIDF().calculateTFIDF()
  
  #Finds the index of a word in the unique word list, or returns -1 if not found
  def findWordIndex(self, word):
    if word in self.uniqueWordList:
      return self.uniqueWordList[word]
    return -1
    # try:
    #   wordIndex = self.uniqueWordList.index(word)
    #   return wordIndex
    # except ValueError:
    #   return -1

  #Calculates Term Frequency
  def calculateTF(self, showTime=False):
    startTime = time.time()
    for i in range(0, self.docCount):
      document = self.documents[i]
      docWords = document.getField('BODY').split()
      for word in docWords:
        index = self.findWordIndex(word)
        if index!=-1:
          self.allTFs[i][self.uniqueWordList[word]]+=1

      for word in docWords:
        index = self.findWordIndex(word)
        if index != -1:
          self.allTFs[i][index]=math.log(self.allTFs[i][index], 2)+1

    if showTime:
      print('TF Function Runtime: ' + str(round(time.time() - startTime, 3)) + ' seconds')
    return self
  
  #Calculates the Inverse Document Frequency score
  def calculateIDF(self, showTime=False):
    startTime = time.time()
    counts = np.zeros(len(self.allTFs[0]))
    for tf in self.allTFs:
      containedIndexes = np.where(tf>0)
      for index in containedIndexes:
        counts[index]+=1
    
    for i in range(0, len(counts)):
      self.idf[i] = math.log(self.docCount / (counts[i]), 2)
    if showTime:
      print('IDF Function Runtime: ' + str(round(time.time() - startTime, 3)) + ' seconds')
    return self

  #Calculates TFIDF Based on Inputted TF and IDF
  def calculateTFIDF(self, showTime=False):
    startTime = time.time()
    self.tfidf = np.multiply(self.allTFs, self.idf)
    if showTime:
      print('TFIDF Function Runtime: ' + str(round(time.time() - startTime, 3)) + ' seconds')
    return self
  
  #Calculates the similarity between each of the vectors using the cosine similarity formula
  def calculateCosineSimilarity(self):
    dotProd = np.dot(self.tfidf, self.tfidf.T)
    squaredMatrix = np.diag(dotProd)
    inversedSquare = 1/squaredMatrix
    inversedSquare[np.isinf(inversedSquare)] = 0
    inversedUnsquare = np.sqrt(inversedSquare)
    self.similarityMatrix = dotProd * inversedUnsquare
    self.similarityMatrix = self.similarityMatrix.T * inversedUnsquare

  #Prints the value in any of the three fields
  def printVal(self, valName, index=0):
    np.set_printoptions(threshold=np.inf)
    if(valName == 'tfidf'):
      print(self.tfidf[index])
    elif valName == 'tf':
      print(self.allTFs[index])
    elif valName == 'idf':
      print(self.idf)
    elif valName == 'sim':
      print(self.similarityMatrix[index])
    return self

