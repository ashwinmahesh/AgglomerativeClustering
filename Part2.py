import time
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, single, complete, cut_tree
from matplotlib import pyplot as plt
import numpy as np

def displaySingleDendogram(singleCluster, docCount):
  plt.figure(figsize=(25, 10))
  plt.title('Single Hierarchical Clustering Dendrogram')
  plt.xlabel('Document')
  plt.ylabel('Similarity')
  labelList = range(0, docCount)
  dg = dendrogram(singleCluster, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
  plt.show()

def part2(computedTFIDF):
  startTime = time.time()
  runningTotalTime=0
  print("Executing code for Part 2...")

  print("Creating and cutting single link clusters...")
  singleCluster = single(computedTFIDF.similarityMatrix)
  singleClusterCut = cut_tree(singleCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])
  singleClusterTime = round(time.time() - startTime, 3)
  runningTotalTime+=singleClusterTime
  print("Time: " + str(singleClusterTime) + " seconds")

  print("Creating list of single link clusters each document is contained in...")
  documentClusters=[]
  for i in range(0, computedTFIDF.docCount):
    documentClusters.append({'id':computedTFIDF.documents[i].getField('NEWID'), 'clusters':{}})
  for clusterCut in singleClusterCut:
    for i in range(0, len(clusterCut)):
      if clusterCut[i] not in documentClusters[i]['clusters']:
        documentClusters[i]['clusters'][clusterCut[i]]=True
  singleTrackingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=singleTrackingTime
  print("Time: " + str(singleTrackingTime) + " seconds")

  print("Converting singe link clusters from dictionary to list...")
  for document in documentClusters:
    document['clusters']=document['clusters'].keys()
  singleConversionTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=singleTrackingTime
  print("Time: " + str(singleConversionTime) + " seconds")

  print("Writing single link clusters to file...")
  singleLinkOutputFile = open('single.txt', 'w')
  for document in documentClusters:
    singleLinkOutputFile.write(f'{document["id"]} ')
    for cluster in document['clusters']:
      singleLinkOutputFile.write(f'{str(cluster)} ')
    singleLinkOutputFile.write('\n')
  singleLinkOutputFile.close()
  singleWritingTime = round(time.time() - startTime - runningTotalTime, 3)
  runningTotalTime+=singleWritingTime
  print("Time: " + str(singleWritingTime) + " seconds")
  
  # print(documentClusters)
  # np.set_printoptions(threshold=np.inf)
  # print(singleClusterCut[65:70])
  # displaySingleDendogram(singleCluster, computedTFIDF.docCount)
  #Correct so far




  print('\nPart 2 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")
