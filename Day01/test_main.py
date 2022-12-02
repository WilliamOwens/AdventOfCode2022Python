from main import solution1, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution1(_input) == 24000
    print("Passed Day 01 Part 1")

if __name__ == "__main__":
    test()