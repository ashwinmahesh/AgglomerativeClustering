import time
from Part1 import part1
from Part2 import part2

startTime = time.time()

print("\nAgglomerative Clustering by Ashwin Mahesh (@mahesh2)\n")

# computedTFIDF = part1()
# part2(computedTFIDF)
part2('a')

print('PROGRAM HAS TERMINATED EXECUTION')
print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds")
