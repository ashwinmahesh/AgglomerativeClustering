import time
import math

#Gets the number of total unique topics among all clusters in a given clustering method
def extractUniqueTopics(clusteringMethod):
  uniqueTopics={}
  for doc in clusteringMethod:
    topics = doc['topics']
    for topic in topics:
      if topic not in uniqueTopics:
        uniqueTopics[topic]=0
      uniqueTopics[topic]+=1
  return uniqueTopics

#Gets all of the documents in each cluster
def getDocsByCluster(clustering):
  allClusters={}
  docCount=0
  for document in clustering:
    if document['topics']!='':  
      docCount+=1
      for cluster in document['clusters']:
        if cluster not in allClusters:
          allClusters[cluster]=[]
        allClusters[cluster].append(document)
        
  return allClusters, docCount

#Removes clusters from list that contain greater more documents than the proportion
def cleanupClusters(clusterList, proportion, docCount):
  removeValues=[]
  for cluster in clusterList:
    if len(clusterList[cluster])>proportion*docCount:
      removeValues.append(cluster)
  for value in removeValues:
    del clusterList[value]
  return clusterList

#Gets the number of documents of each topic in a cluster
def getTopicCountByCluster(cluster):
  topics={}
  for doc in cluster:
    for topic in doc['topics']:
      if topic not in topics:
        topics[topic]=0
      topics[topic]+=1
  return topics

def getMaxAndSecondMaxTopics(clusterTopics):
  maxKey=''
  maxCount=0
  secondMaxKey=''
  secondMaxCount=0
  for topic in clusterTopics:
    # print(topic)
    if clusterTopics[topic] > maxCount:
      secondMaxKey = maxKey
      secondMaxCount = maxCount
      maxCount=clusterTopics[topic]
      maxKey=topic

    elif clusterTopics[topic] > secondMaxCount:
      secondMaxCount = clusterTopics[topic]
      secondMaxKey = topic

  return maxKey, maxCount, secondMaxKey, secondMaxCount

#Calculates the similarity at each cluster by using the topics
#Needs input from getTopicCountByCluster Function
#Maximum Topic / 2nd highest topic * log2(Total Number of documents in cluster)+1
def calculateSimilarityAtOneCluster(cluster, numDocsInCluster):
  maxKey, maxCount, secondMaxKey, secondMaxCount = getMaxAndSecondMaxTopics(cluster)
  secondMaxCount = 1 if secondMaxCount==0 else secondMaxCount
  return maxCount * (math.log(numDocsInCluster, 2) +1) / secondMaxCount


#Sums up the similarities for all the clusters then divides by some normalizing factor?
def evaluate(totalSimilarity):
  return totalSimilarity

#Test function used as a playground
def test(clusteringOutput):
  for doc in clusteringOutput:
    print(doc['topics'])

  
def part3(parsedDocuments, singleClustering, completeClustering):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")

  print("Beginning Evaluation of Clustering...")
  clustersWithDocuments, docCount = getDocsByCluster(singleClustering)
  removedHigherLevelClustersSingle = cleanupClusters(clustersWithDocuments, 0.4, docCount)
  # for clusterID in removedHigherLevelClustersSingle:
  #   print(f'{clusterID}: {getTopicCountByCluster(removedHigherLevelClustersSingle[clusterID])}')
  totalSimilarity_Single=0
  # for clusterID in clustersWithDocuments:
  for clusterID in removedHigherLevelClustersSingle:
    topicForCluster = getTopicCountByCluster(removedHigherLevelClustersSingle[clusterID])
    totalSimilarity_Single+=calculateSimilarityAtOneCluster(topicForCluster, len(removedHigherLevelClustersSingle[clusterID]))
  print(evaluate(totalSimilarity_Single))

  # print(removedHigherLevelClustersSingle)



  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")