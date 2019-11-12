import time
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, single, complete, cut_tree
from matplotlib import pyplot as plt
import numpy as np

def printSingleDendogram(singleCluster, docCount):
  plt.figure(figsize=(25, 10))
  plt.title('Single Hierarchical Clustering Dendrogram')
  plt.xlabel('Document')
  plt.ylabel('Similarity')
  labelList = range(0, docCount)
  dg = dendrogram(singleCluster, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
  plt.show()

def part2(computedTFIDF):
  startTime = time.time()

  print("Executing code for Part 2...")

  singleCluster = single(computedTFIDF.similarityMatrix)
  singleClusterCut = cut_tree(singleCluster, n_clusters=[i for i in range(0, computedTFIDF.docCount-1)])

  documentClusters={}
  for document in computedTFIDF.documents:
    print(document.getAllFields())
  # np.set_printoptions(threshold=np.inf)
  # print(singleClusterCut[65:70])
  # printSingleDendogram(singleCluster, computedTFIDF.docCount)
  #Correct so far




  print('\nPart 2 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")
