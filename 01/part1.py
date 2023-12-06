
def get_calibration_value(inp: str):
    left = 0
    right = len(inp)-1
    
    while not inp[left].isnumeric() or not inp[right].isnumeric():
        if not inp[left].isnumeric():
            left += 1
        if not inp[right].isnumeric():
            right -= 1

    return int(inp[left] + inp[right])
        
def main():
    FILENAME = "input.txt"
    
    sum_calibration = 0
    with open(FILENAME, "r") as f:
        for line in f:
            sum_calibration += get_calibration_value(line)
    
    print(f"Ans: {sum_calibration}")

if __name__ == "__main__":
    main()