import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from XMLParser import XMLParse

def removeStopwords(text):
  porterStemmer = PorterStemmer()
  stopWords = set(stopwords.words('english'))
  tokenedText = word_tokenize(text)
  #print(tokenedText)
  newBody=''
  for word in tokenedText:
    if word not in stopWords:
      newBody+=porterStemmer.stem(word)
      newBody+=' '
  return newBody  

if __name__ == '__main__':
  print("Agglomerative Clustering")
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm")

  for i in range(0, 5):
    print(i)
    print(removeStopwords(values[i]["BODY"]))

