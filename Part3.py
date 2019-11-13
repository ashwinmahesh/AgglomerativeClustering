import time

def test(documents):
  for i in range(0, 10):
    print(documents[i].extractSubElements('TOPICS'))

def part3(parsedDocuments, singeClustering, completeClustering):
  startTime = time.time()
  runningTotalTime=0

  print("Executing code for Part 3...\n")

  print("Beginning Evaluation of Clustering...")
  evalTime = round(time.time() - startTime, 3)
  runningTotalTime+=evalTime
  print("Time: " + str(evalTime) + " seconds")

  test(parsedDocuments)

  print('\nPart 3 Complete')
  print("Execution Time: " + str(round(time.time() - startTime, 3)) + " seconds\n")