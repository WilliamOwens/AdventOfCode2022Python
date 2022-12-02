import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return _input

def solution1(l):
  largestCalorieLoad = 0
  currentCalorieLoad = 0
  for i in range(0, len(l)):
    if not l[i]:
      if (currentCalorieLoad > largestCalorieLoad):
        largestCalorieLoad = currentCalorieLoad
      currentCalorieLoad = 0
    else:
      currentCalorieLoad += int(l[i])
  return largestCalorieLoad

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution1(_input))