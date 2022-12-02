import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    _input.append('')
    return _input

def solution(l, toFind):
  largestCalorieLoad = [0] * toFind
  currentCalorieLoad = 0
  for i in range(0, len(l)):
    if not l[i]:
      currentMin = min(largestCalorieLoad)
      if (currentCalorieLoad > currentMin):
        largestCalorieLoad[largestCalorieLoad.index(currentMin)] = currentCalorieLoad
      currentCalorieLoad = 0
    else:
      currentCalorieLoad += int(l[i])
  return sum(largestCalorieLoad)

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(solution(_input, 1))
    print(solution(_input, 3))