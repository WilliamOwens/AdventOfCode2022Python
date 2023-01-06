import os

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input[0]

def solution(buffer, inputLength):
  tempList = []
  i=0
  while i < len(buffer):
    if buffer[i] not in tempList:
      tempList.append(buffer[i])
      i+=1
      if len(tempList) == inputLength:
        return i
    else:
      i= (i - len(tempList) + 1)
      tempList = []
      tempList.append(buffer[i])
      i+=1
  return -1

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution(_input, 4))
  print(solution(_input, 14))
