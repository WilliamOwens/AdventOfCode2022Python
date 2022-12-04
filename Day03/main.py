import os

ASCII_DIFFERENCE_SMALL = 96
ASCII_DIFFERENCE_BIG = 38

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input

def calculateRunningTotal(inputSet):
  partialRunningTotal = 0
  for j in inputSet:
    if (ord(j) > 90):
      partialRunningTotal += ord(j) - ASCII_DIFFERENCE_SMALL
    else:
      partialRunningTotal += ord(j) - ASCII_DIFFERENCE_BIG
  return partialRunningTotal

def solution1(l):
  runningTotal = 0
  for i in range(0, len(l)):
    halfLength = int(len(l[i])/2)
    unionGroup = set(l[i][:halfLength]) & set(l[i][halfLength:])
    runningTotal += calculateRunningTotal(unionGroup)
  return runningTotal

def solution2(l):
  runningTotalPartTwo = 0
  for i in range(0, len(l), 3):
    setOfAllThree = set(l[i]) & set(l[i+1]) & set(l[i+2])
    runningTotalPartTwo += calculateRunningTotal(setOfAllThree)
  return runningTotalPartTwo

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))
    print(solution2(_input))