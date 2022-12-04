import os

ASCII_DIFFERENCE_SMALL = 96
ASCII_DIFFERENCE_BIG = 38

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input

def solution1(l):
  runningTotal = 0
  for i in range(0, len(l)):
    halfLength = int(len(l[i])/2)
    unionGroup = set(set(l[i][:halfLength]).intersection(set(l[i][halfLength:])))
    for j in unionGroup:
      if (ord(j) > 90):
        runningTotal += ord(j) - ASCII_DIFFERENCE_SMALL
      else:
        runningTotal += ord(j) - ASCII_DIFFERENCE_BIG
  return runningTotal

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))