import os

def readFile(fileName):
  dir = os.path.abspath(os.path.dirname(__file__))
  with open(os.path.join(dir, fileName)) as file:
    _input = file.read().splitlines()
  return _input

if __name__ == "__main__":
    _input = readFile("input.txt")
    print(_input)