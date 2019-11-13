import time
from Part1 import part1
from Part2 import part2
from Part3 import part3

startTime = time.time()

print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

computedTFIDF = part1(100)
singleDocClusters, completeDocClusters = part2(computedTFIDF)
part3()

print('PROGRAM HAS TERMINATED EXECUTION')
print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")
