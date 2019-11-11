from XMLParser import XMLParse

if __name__ == '__main__':
  print("Agglomerative Clustering")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm")

  for i in range(0, 5):
    print(i)
    print(values[i]["BODY"])

