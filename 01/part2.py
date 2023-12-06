
digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def value_at(inp: str, index: int):
    result = inp[index]

    for word, digit in digits.items():
        if inp[index:index+len(word)] == word:
            result = str(digit)
            break

    return result

def get_calibration_value(inp: str):
    left = 0
    right = len(inp)-1
    
    while not value_at(inp, left).isnumeric():
        left += 1
    
    while not value_at(inp, right).isnumeric():
        right -= 1
    
    return int(value_at(inp, left) + value_at(inp, right))

def main():
    FILENAME = "input.txt"
    
    sum_calibration = 0
    with open(FILENAME, "r") as f:
        for line in f:
            result = get_calibration_value(line.strip())
            
            print(result)
            
            sum_calibration += result
            
    print(f"Ans: {sum_calibration}")

if __name__ == "__main__":
    main()