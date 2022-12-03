from main import solution1, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution1(_input) == 15
    print("Passed Day 02 Part 1")
if __name__ == "__main__":
    test()