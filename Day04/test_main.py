from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, True) == 2
    print("Passed Day 04 Part 1")
    assert solution(_input, False) == 4
    print("Passed Day 04 Part 2")
if __name__ == "__main__":
    test()