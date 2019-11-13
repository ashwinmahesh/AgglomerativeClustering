import time

def part3():
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")

  print("Beginning Evaluation of Clustering...")
  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")