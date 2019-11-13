import time

def extractUniqueTopics(parsedDocuments):
  uniqueTopics={}
  for doc in parsedDocuments:
    topics = doc.extractSubElements('TOPICS')
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
  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  # print(getAllDocsInEachCluster(completeClustering))
  # test(singleClustering)
  # print(extractUniqueTopics(parsedDocuments))
  # test(parsedDocuments)

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")