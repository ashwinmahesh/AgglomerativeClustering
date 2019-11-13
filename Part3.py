import time

def extractUniqueTopics(clusteringMethod):
  uniqueTopics={}
  for doc in clusteringMethod:
    topics = doc['topics']
    for topic in topics:
      if topic not in uniqueTopics:
        uniqueTopics[topic]=0
      uniqueTopics[topic]+=1
  return uniqueTopics

def getAllDocsInEachCluster(clustering):
  allClusters={}
  for document in clustering:
    for cluster in document['clusters']:
      if cluster not in allClusters:
        allClusters[cluster]=[]
      allClusters[cluster].append(document['id'])
  return allClusters

def cleanupClusters(clusterList, proportion, docCount):
  removeValues=[]
  for cluster in clusterList:
    if len(clusterList[cluster])>proportion*docCount:
      removeValues.append(cluster)
  for value in removeValues:
    del clusterList[value]
  return clusterList

def evaluate(clusteringMethod):
  return True

def test(clusteringOutput):
  for doc in clusteringOutput:
    print(doc['topics'])
  # for i in range(0, 10):
  #   print(documents[i].extractSubElements('TOPICS'))
  
def part3(parsedDocuments, singleClustering, completeClustering):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")

  print("Beginning Evaluation of Clustering...")
  docsBySingleCluster = getAllDocsInEachCluster(singleClustering)
  removingOvercrowdedSingle = cleanupClusters(docsBySingleCluster, 0.3, len(parsedDocuments))
  print(removingOvercrowdedSingle)
  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  # print(getAllDocsInEachCluster(completeClustering))
  # test(singleClustering)
  # print(extractUniqueTopics(singleClustering))
  # test(parsedDocuments)

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")