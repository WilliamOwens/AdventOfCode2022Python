import os
import re

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
    if fullOverlap:
      if (((line[0] >= line[2]) & (line[1] <= line[3])) | (((line[2] >= line[0]) & (line[3] <= line[1])))):
        runningTotal += 1
    else:
      if ((line[0] <= line[3]) & (line[1] >= line[2])):
        runningTotal += 1
  return runningTotal

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(solution(_input, True))
  print(solution(_input, False))
