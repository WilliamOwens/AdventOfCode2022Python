import os
from collections import deque
import re


def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input

def getMovesInput(d):
  moveInputArray = []
  for line in d:
    moveInputArray.append([int(i) for i in line.split() if i.isdigit()])
  return moveInputArray

def getStacksInput(d):
  inputStacks = []
  numberOfColumns = int((int(len(d[0])) + 1) / 4)
  for _ in range(numberOfColumns):
    inputStacks.append([])
  for char in range(numberOfColumns):
    for level in reversed(range(len(d))):
      crate = d[level][char * 4 + 1]
      if (crate != ' '):
        inputStacks[char].append(crate)
  return inputStacks

def solution(l, newModel):
  stacks = getStacksInput(l[:l.index('') - 1])
  movesData = getMovesInput(l[l.index('') + 1:])
  if (newModel):
    for moveSet in movesData:
      tempList = []
      for _ in range(moveSet[0]):
        tempList.append(stacks[(moveSet[1] - 1)].pop())
      for _ in range(len(tempList)):
        stacks[(moveSet[2] - 1)].append(tempList.pop())
  else:
    for moveSet in movesData:
      for _ in range(moveSet[0]):
        stacks[(moveSet[2] - 1)].append(stacks[(moveSet[1] - 1)].pop())

  runningTotal = ''
  for stack in stacks:
    runningTotal += stack.pop()
  return runningTotal


if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution(_input, False))
  print(solution(_input, True))
