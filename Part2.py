import time
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, single, complete, cut_tree
from matplotlib import pyplot as plt
import numpy as np

def writeToFile(documentClusters, filename):
  outputFile = open(filename, 'w')
  outputFile.write('NEWID\tclustersID\n')

  for document in documentClusters:
    outputFile.write(f'{document["id"]}\t')
    for cluster in document['clusters']:
      outputFile.write(f'{str(cluster)} ')
    outputFile.write('\n')
  outputFile.close()

def displaySingleDendogram(singleCluster, docCount):
  plt.figure(figsize=(25, 10))
  plt.title('Single Hierarchical Clustering Dendrogram')
  plt.xlabel('Document')
  plt.ylabel('Similarity')
  labelList = range(0, docCount)
  dg = dendrogram(singleCluster, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
  plt.show()

def createDocumentCluster(clusterAfterCut, computedTFIDF):
  documentClusters=[]
  allClusters={}
  for i in range(0, computedTFIDF.docCount):
    documentClusters.append({'id':computedTFIDF.documents[i].getField('NEWID'), 'clusters':[], 'topics':computedTFIDF.documents[i].extractSubElements('TOPICS')})

  for i in range(0, len(clusterAfterCut)):
    if clusterAfterCut[i]+1 not in allClusters:
      allClusters[clusterAfterCut[i]+1]=True
    for clusterID in list(allClusters.keys()):
      documentClusters[i]['clusters'].append(clusterID)

  return documentClusters

def part2(computedTFIDF):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 2...\n")

  print("Creating and cutting single link clusters...")
  singleCluster = single(computedTFIDF.similarityMatrix)
  singleClusterCut = cut_tree(singleCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])
  singleClusterTime = round(time.time() - startTime, 3)
  runningTotalTime+=singleClusterTime
  print("Time: " + str(singleClusterTime) + " seconds")

  print("Creating list of single link clusters each document is contained in...")
  finalSingleClustering = singleClusterCut[len(singleClusterCut)-1]
  documentClusters=createDocumentCluster(finalSingleClustering, computedTFIDF)
  singleTrackingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=singleTrackingTime
  print("Time: " + str(singleTrackingTime) + " seconds")

  print("Writing single link clusters to file...")
  writeToFile(documentClusters, 'single.txt')
  singleWritingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=singleWritingTime
  print("Time: " + str(singleWritingTime) + " seconds")

  print("Creating and cutting complete link clusters...")
  completeCluster = complete(computedTFIDF.similarityMatrix)
  completeClusterCut = cut_tree(completeCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])
  completeClusterTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=completeClusterTime
  print("Time: " + str(completeClusterTime) + " seconds")

  print("Creating list of complete link clusters each document is contained in...")
  finalCompleteClustering = completeClusterCut[len(completeClusterCut)-1]
  completeDocumentClusters=createDocumentCluster(finalCompleteClustering, computedTFIDF)
  completeTrackingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=completeTrackingTime
  print("Time: " + str(completeTrackingTime) + " seconds")

  print("Writing complete link clusters to file...")
  writeToFile(completeDocumentClusters, 'complete.txt')
  completeWritingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=completeWritingTime
  print("Time: " + str(completeWritingTime) + " seconds")

  print('\nPart 2 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")
  
  return documentClusters, completeDocumentClusters
