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

#Returns the topics with the highest and second highest number of documents
def getMaxAndSecondMaxTopics(clusterTopics):
  maxKey=''
  maxCount=0
  secondMaxKey=''
  secondMaxCount=0
  for topic in clusterTopics:
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
#Maximum Topic Count/ 2nd highest topic Count * [log2(Total Number of documents in cluster)+1]
def calculateSimilarityAtOneCluster(cluster, numDocsInCluster):
  maxKey, maxCount, secondMaxKey, secondMaxCount = getMaxAndSecondMaxTopics(cluster)
  secondMaxCount = 1 if secondMaxCount==0 else secondMaxCount
  return maxCount * (math.log(numDocsInCluster, 2) +1) / secondMaxCount

#Sums up the similarities for all the clusters then divides by some normalizing factor?
def evaluate(clusteringMethod):
  clustersWithDocuments, docCount = getDocsByCluster(clusteringMethod)
  removedHigherLevelClusters = cleanupClusters(clustersWithDocuments, 0.5, docCount)

  totalSimilarity=0
  for clusterID in removedHigherLevelClusters:
    topicForCluster = getTopicCountByCluster(removedHigherLevelClusters[clusterID])
    totalSimilarity+=calculateSimilarityAtOneCluster(topicForCluster, len(removedHigherLevelClusters[clusterID]))

  return totalSimilarity/docCount

def part3(singleClustering, completeClustering):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")
  print("Evaluating Single and Complete Link Clustering...")
  singleEvalScore = evaluate(singleClustering)
  completeEvalScore=evaluate(completeClustering)
  print(f'Single Linkage Score: {singleEvalScore}')
  print(f'Complete Linkage Score: {completeEvalScore}')
  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")
  return singleEvalScore, completeEvalScore