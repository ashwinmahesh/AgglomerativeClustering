import time

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

#Calculates the similarity at each cluster by using the topics
#Needs input from getTopicCountByCluster Function
def calculateSimilarityAtOneCluster(cluster):
  return 1

#Sums up the similarities for all the clusters then divides by some normalizing factor?
def evaluate(clusteringMethod):
  return True

#Test function used as a playground
def test(clusteringOutput):
  for doc in clusteringOutput:
    print(doc['topics'])

  
def part3(parsedDocuments, singleClustering, completeClustering):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")

  print("Beginning Evaluation of Clustering...")
  docsBySingleCluster, docCount = getDocsByCluster(singleClustering)
  # removedHigherLevelClustersSingle = cleanupClusters(docsBySingleCluster, 0.4, docCount)
  # for clusterID in removedHigherLevelClustersSingle:
  #   print(f'{clusterID}: {getTopicCountByCluster(removedHigherLevelClustersSingle[clusterID])}')

  # print(removedHigherLevelClustersSingle)



  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")