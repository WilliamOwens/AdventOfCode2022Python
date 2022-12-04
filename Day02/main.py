import os

RPS_TRANSLATION = {
  'A': 0, #rock
  'X': 0,
  'B': 1, #paper
  'Y': 1,
  'C': 2, #scissors
  'Z': 2,
}
SCORING_TRANSLATION = {
  -2: 6,
  -1: 0,
  0: 3,
  1: 6,
  2: 0,
}

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input

def solution1(l):
  runningTotal = 0
  for i in range(0, len(l)):
    runningTotal += SCORING_TRANSLATION[int(RPS_TRANSLATION[l[i][2]]) - int(RPS_TRANSLATION[l[i][0]])] + int(RPS_TRANSLATION[l[i][2]]) + 1
  return runningTotal

def solution2(l):
  runningTotal = 0
  for i in range(0, len(l)):
    opponentThrow = l[i][0]
    myOutcome = l[i][2]
    runningTotal += (RPS_TRANSLATION[myOutcome] * 3)
    if (l[i][2] == 'Y'):
      runningTotal += int(RPS_TRANSLATION[opponentThrow])
    if (l[i][2] == 'X'):
      runningTotal += ((RPS_TRANSLATION[opponentThrow] + 2) % 3)
    if (l[i][2] == 'Z'):
      runningTotal += ((RPS_TRANSLATION[opponentThrow] + 1) % 3)
    runningTotal += 1 # 
  return runningTotal

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))
    print(solution2(_input))
# okay so how cool is this??