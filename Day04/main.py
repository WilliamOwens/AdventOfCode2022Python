import os, re

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return prepData(_input)

def prepData(d):
  return [[int(letter) for letter in re.split('-|,', line)] for line in d]

def solution(l, fullOverlap):
  runningTotal = 0
  for line in l:
    if not fullOverlap:
      if ((line[0] <= line[3]) & (line[1] >= line[2])):
        runningTotal += 1
    else:
      firstSection = line[1] - line[0]
      secondSection = line[3] - line[2]
      if (firstSection == secondSection):
        if (line[0] == line[2]):
          runningTotal += 1
      else:
        if firstSection > secondSection:
          LARGER_GAP, LARGER_START, SMALLER_GAP, SMALLER_START = firstSection, line[0], secondSection, line[2]
        else:
          LARGER_GAP, LARGER_START, SMALLER_GAP, SMALLER_START = secondSection, line[2], firstSection, line[0]
        if ((SMALLER_START >= LARGER_START) & (SMALLER_START <= (LARGER_START + (LARGER_GAP - SMALLER_GAP)))):
          runningTotal += 1
  return runningTotal

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution(_input, True))
    print(solution(_input, False))