import os

RPS_TRANSLATION = {
  'A': 1, #rock
  'X': 1,
  'B': 2, #paper
  'Y': 2,
  'C': 3, #scissors
  'Z': 3,
}
SCORING_TRANSLATION = {
  -2: 6,
  -1: 0,
  -0: 3,
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
    runningTotal += SCORING_TRANSLATION[int(RPS_TRANSLATION[l[i][2]]) - int(RPS_TRANSLATION[l[i][0]])] + int(RPS_TRANSLATION[l[i][2]])
  return runningTotal

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))