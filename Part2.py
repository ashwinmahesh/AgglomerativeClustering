import time
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, single, complete, cut_tree
from matplotlib import pyplot as plt
import numpy as np

def writeToFile(documentClusters, filename):
  outputFile = open(filename, 'w')
  for document in documentClusters:
    outputFile.write(f'{document["id"]} ')
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

def createDocumentCluster(clustersAfterCut, computedTFIDF):
  documentClusters=[]
  for i in range(0, computedTFIDF.docCount):
    documentClusters.append({'id':computedTFIDF.documents[i].getField('NEWID'), 'clusters':{}})
  for clusterCut in clustersAfterCut:
    for i in range(0, len(clusterCut)):
      if clusterCut[i] not in documentClusters[i]['clusters']:
        documentClusters[i]['clusters'][clusterCut[i]]=True
  for document in documentClusters:
    document['clusters']=document['clusters'].keys()
  return documentClusters

def part2(computedTFIDF, calculateSingle=True, calculateComplete=True):
  startTime = time.time()
  runningTotalTime=0

  # np.set_printoptions(threshold=np.inf)
  print("Executing code for Part 2...\n")
  if calculateSingle:
    print("Creating and cutting single link clusters...")
    singleCluster = single(computedTFIDF.similarityMatrix)
    singleClusterCut = cut_tree(singleCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])
    singleClusterTime = round(time.time() - startTime, 3)
    runningTotalTime+=singleClusterTime
    print("Time: " + str(singleClusterTime) + " seconds")

    # print(singleClusterCut[len(singleClusterCut)-2])

    print("Creating list of single link clusters each document is contained in...")
    documentClusters=createDocumentCluster(singleClusterCut, computedTFIDF)
    singleTrackingTime = round(time.time() - startTime - runningTotalTime, 3)
    runningTotalTime+=singleTrackingTime
    print("Time: " + str(singleTrackingTime) + " seconds")

    print("Writing single link clusters to file...")
    writeToFile(documentClusters, 'single.txt')
    singleWritingTime = round(time.time() - startTime - runningTotalTime, 3)
    runningTotalTime+=singleWritingTime
    print("Time: " + str(singleWritingTime) + " seconds")
  
  if calculateComplete:
    print("Creating and cutting complete link clusters...")
    completeCluster = complete(computedTFIDF.similarityMatrix)
    completeClusterCut = cut_tree(completeCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])
    completeClusterTime = round(time.time() - startTime - runningTotalTime, 3)
    runningTotalTime+=completeClusterTime
    print("Time: " + str(completeClusterTime) + " seconds")

    # print(completeClusterCut[len(completeClusterCut)-1])

    print("Creating list of complete link clusters each document is contained in...")
    completeDocumentClusters=createDocumentCluster(completeClusterCut, computedTFIDF)
    completeTrackingTime = round(time.time() - startTime - runningTotalTime, 3)
    runningTotalTime+=completeTrackingTime
    print("Time: " + str(completeTrackingTime) + " seconds")

    print("Writing complete link clusters to file...")
    writeToFile(completeDocumentClusters, 'complete.txt')
    completeWritingTime = round(time.time() - startTime - runningTotalTime, 3)
    runningTotalTime+=completeWritingTime
    print("Time: " + str(completeWritingTime) + " seconds")
  
  #Correct so far




  print('\nPart 2 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")
