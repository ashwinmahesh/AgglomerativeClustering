import time
from Part1 import part1
from Part2 import part2

startTime = time.time()

print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

computedTFIDF = part1(100)
part2(computedTFIDF, calculateSingle=True, calculateComplete=True)

print('PROGRAM HAS TERMINATED EXECUTION')
print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")
