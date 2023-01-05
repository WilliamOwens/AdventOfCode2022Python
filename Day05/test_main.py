from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, False) == 'CMZ'
    print("Passed Day 05 Part 1")
    _input = readFile("test_input.txt")
    assert solution(_input, True) == 'MCD'
    print("Passed Day 05 Part 2")
if __name__ == "__main__":
    test()