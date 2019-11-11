import math
import numpy as np

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
    try:
      wordIndex = self.uniqueWordList.index(word)
      return wordIndex
    except ValueError:
      return -1

  #Calculates Term Frequency
  def calculateTF(self):
    for i in range(0, self.docCount):
      document = self.documents[i]
      docWords = document.getField('BODY').split()
      for word in docWords:
        index = self.findWordIndex(word)
        if index != -1:
          self.allTFs[i][index]+=1

      for word in docWords:
        index = self.findWordIndex(word)
        if index != -1:
          self.allTFs[i][index]=math.log(self.allTFs[i][index], 2)+1
    return self
  
  #Calculates the Inverse Document Frequency score
  def calculateIDF(self):
    counts = np.zeros(len(self.allTFs[0]))
    for tf in self.allTFs:
      containedIndexes = np.where(tf>0)
      for index in containedIndexes:
        counts[index]+=1
    
    for i in range(0, len(counts)):
      self.idf[i] = math.log(self.docCount / (counts[i]), 2)

    return self

  #Calculates TFIDF Based on Inputted TF and IDF
  def calculateTFIDF(self):
    self.tfidf = np.multiply(self.allTFs, self.idf)
    return self
  
  #Calculates the similarity between each of the vectors using the cosine similarity formula
  def calculateCosineSimilarity(self):
    # squaredMatrix = np.square(self.tfidf)
    # sumMatrix = self
    # print(np.dot(self.tfidf, self.tfidf))
    # self.similarityMatrix = np.sum(self.tfidf*self.tfidf) / 
    for i in range(0, self.docCount):
      doc1Squared = np.multiply(self.tfidf[i], self.tfidf[i])
      doc1SquaredSum = np.sum(doc1Squared)
      for j in range(0, self.docCount):
        if i == j:
          continue
        top = np.dot(self.tfidf[i], self.tfidf[j])

        doc2Squared = np.multiply(self.tfidf[j], self.tfidf[j])
        doc2SquaredSum= np.sum(doc2Squared)

        bottom = math.sqrt(doc1SquaredSum * doc2SquaredSum)
        self.similarityMatrix[i][j]=top/bottom
    return self

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

