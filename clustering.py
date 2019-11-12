import time
from Part1 import part1

startTime = time.time()

print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

computedTFIDF = part1()

print('PROGRAM HAS TERMINATED EXECUTION')
print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")
