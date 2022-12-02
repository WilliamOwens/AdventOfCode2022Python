from main import solution, readFile

def test():
    _input = readFile("test_input.txt")
    assert solution(_input, 1) == 24000
    print("Passed Day 01 Part 1")
    assert solution(_input, 3) == 45000
    print("Passed Day 01 Part 2")

if __name__ == "__main__":
    test()