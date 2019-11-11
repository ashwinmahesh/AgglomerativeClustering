import re

#Gets the next token in the list, can confirm it works in the base case
def getNextToken(text, currentIndex):
  newIndex = currentIndex
  token = ''
  increment=0
  while(text[currentIndex+increment]==' ' or text[currentIndex+increment]=='\n'):
    increment += 1

  if(text[currentIndex+increment]=='<'):
    while(text[currentIndex+increment]!='>'):
      token+=text[currentIndex+increment]
      increment+=1
    token+=text[currentIndex+increment]
    newIndex += (increment+1)
  
  else:
    while(text[currentIndex+increment]!=' ' and text[currentIndex+increment]!='\n' and text[currentIndex+increment]!='\0' and text[currentIndex+increment]!='<'):
      token+=text[currentIndex+increment]
      increment+=1
    newIndex += increment
  return token, newIndex

#Checks if it is a tag, or not
def isTag(text):
  if(text[0]=='<'):
    return True
  return False

#Checks if the tag is an open or a close tag
def isOpenTag(text):
  if(text[0]=='<' and text[1]=='/'):
    return False
  return True

##Make opened tags a stack, if there is anything in the stack thats not reuters, then push the text into that stack
def HTMLParser(filePath):
  file = open(filePath)
  file.readline()
  fileText = file.read()

  index = 0
  text, index = getNextToken(fileText, 0)
  for i in range(0, 4):
    text, index = getNextToken(fileText, index)
    print(text)
  # openTag = re.compile("<[A-Za-z]+")

  # currentTag=''
  # output=[]
  # currentIndex=0
  # nextIndexValue = ''
  # for i in range(0, len(fileText)):
  #   current = fileText[i]


  #   if(current == '<' and currentTag == '' and fileText[i+1]!='/'):
  #     i+=1
  #     checkTag = ''
  #     while(fileText[i]!=' '):
  #       checkTag+=fileText[i]
  #       i+=1
  #     while(fileText[i]!='>'):
  #       i+=1
      
  #     if(checkTag == 'REUTERS'):
  #       output.append({})
  #     else:
  #       currentTag=checkTag
      
  #     continue

  #   if(current == '<' and fileText[i+1]=='/' and currentTag==''):
  #     currentIndex+=1
  #     i+=1
  #     while(fileText[i]!='>'):
  #       i+=1
  #     continue

  #   if(current == '<' and fileText[i+1]=='/' and currentTag != ''):
  #     output[currentIndex][currentTag] = nextIndexValue
  #     continue
    
  #   nextIndexValue+=current
    




if __name__ == "__main__":
  print(HTMLParser("/homes/cs473/project2/reut2-subset.sgm"))