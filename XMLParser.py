class XMLDoc:
  def __init__(self, initialTags):
    self.tags=initialTags

  def hasField(self, fieldName):
    if fieldName in self.tags:
      return True
    return False

  def getField(self, fieldName):
    if self.hasField(fieldName):
        return self.tags[fieldName]
    return -1

  def setField(self, tag, value):
    self.tags[tag]=value
    return self

  def removeField(self, tag):
    del self.tags[tag]
    return self

  def getAllFields(self):
    return list(self.tags.keys())

  def getJSON(self):
    return self.tags

  def extractSubElements(self, tag):
    if self.hasField(tag)==False:
      return []
    token, index = getNextToken(self.tags[tag], 0)
    subElements = []
    isOpened=False
    while(token!='' and index!=-1):
      if token=='<D>':
        isOpened = True
      elif token=='</D>':
        isOpened = False
      else:
        if isOpened:
          subElements.append(token)
      token, index = getNextToken(self.tags[tag], index)

    return subElements
    

#Gets the next token in the list, can confirm it works in the base case
def getNextToken(text, currentIndex):
  newIndex = currentIndex
  token = ''
  increment=0
  
  while(currentIndex+increment <len(text) and (text[currentIndex+increment]==' ' or text[currentIndex+increment]=='\n')):
    increment += 1

  if(currentIndex+increment+increment+increment+increment+increment+increment+increment+increment >= len(text)):
    return '', -1

  if(text[currentIndex+increment]=='<'):
    while(text[currentIndex+increment]!='>'):
      token+=text[currentIndex+increment]
      increment+=1
    token+=text[currentIndex+increment]
    newIndex += (increment+1)
  
  else:
    while(currentIndex+increment < len(text) and text[currentIndex+increment]!=' ' and text[currentIndex+increment]!='\n' and text[currentIndex+increment]!='<'):
      token+=text[currentIndex+increment]
      increment+=1
    newIndex += (increment)
  return token, newIndex

#Checks if it is a tag, or not
def isTag(text):
  if text=='<D>' or text=='</D>':
    return False
  if(text[0]=='<'):
    return True
  return False

#Checks if the tag is an open or a close tag
def isOpenTag(text):
  if(text[0]=='<' and text[1]=='/'):
    return False
  return True

#Gets name from the tag
def getTagName(text):
  output=''
  for i in range(1,len(text)):
    if(i==1 and text[i]=='/'):
        i+=1
    if(text[i]==' ' or text[i]=='>'):
        break
    output+=text[i]

  return output

#Extracts additional subinformation from a tag like <Text name=Blah>, this will extract the name field from the text tag
def extractParamsFromTag(tag):
  output={}
  if(tag[0]!='<' and tag[len(tag)-1]!='>'):
    return False
  i=1
  while(tag[i]==' '):
    i+=1
  while(tag[i]!=' '):
    i+=1
  while(tag[i]==' '):
    i+=1
  nextTag, nextVal='', ''
  isTag=True
  
  while(i<len(tag)-1):
    if(tag[i]=='='):
      isTag=not isTag
    elif isTag==False and tag[i]==' ':
      isTag=not isTag
      output[nextTag]=nextVal
      nextTag, nextVal='', ''
    elif isTag:
      nextTag+=tag[i]
    else:
      if tag[i]=='\"':
        i+=1
        continue
      nextVal+=tag[i]
    i+=1
  
  if not isTag and nextTag!='':
    output[nextTag]=nextVal
  return output
      

##Make opened tags a stack, if there is anything in the stack thats not reuters, then push the text into that stack
def XMLParse(filePath,  limit=0, ignoreFirstLine=True):
  file = open(filePath)
  if ignoreFirstLine:
    file.readline()
  fileText = file.read()

  index = 0

  tags = []
  output=[]
  currOutputIndex=-1
  token,index=getNextToken(fileText, index)
  currTextVal=''

  hasLimit = False
  if limit>0:
    hasLimit = True

  while(token!='' and index!=-1):
    if(isTag(token)):
      tag = getTagName(token)
      if(isOpenTag(token)):
        tags.append(tag)
        if(len(tags) == 1):
          if(hasLimit and currOutputIndex>=limit):
            break
          output.append(XMLDoc({}))
          currOutputIndex+=1
          specialTags = extractParamsFromTag(token)
          if specialTags!=False:
            for additionalInfo in specialTags:
              output[currOutputIndex].setField(additionalInfo, specialTags[additionalInfo])
      else:
        output[currOutputIndex].setField(tags[len(tags)-1], currTextVal)
        tags.pop()
        currTextVal=''

    else:
      currTextVal+=token
      currTextVal+=' '
    token,index=getNextToken(fileText, index)
  file.close()
  return output

if __name__ == "__main__":
  values = XMLParse("/homes/cs473/project2/reut2-subset.sgm", 10)
  for i in range(0, 5):
    print(i)
    print(values[i].getField('TOPICS'))
    print(values[i].extractSubElements('TOPICS'))
