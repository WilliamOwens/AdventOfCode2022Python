from main import solution1, solution2, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution1(_input) == 2
    print("Passed Day 04 Part 1")
if __name__ == "__main__":
    test()