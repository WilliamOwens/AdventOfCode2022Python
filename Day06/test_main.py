from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, 4) == 11
    print("Passed Day 06 Part 1")
    _input = readFile("test_input.txt")
    assert solution(_input, 14) == 26
    print("Passed Day 06 Part 2")
if __name__ == "__main__":
    test()