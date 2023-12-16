
def hash_alg(string: str):
    cur = 0
    
    for char in string:
        ascii_code = ord(char)
        cur = ((cur + ascii_code) * 17) % 256
        
    return cur

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        initialization_sequence = f.read().strip().split(",")

    print(initialization_sequence)

    result = sum([hash_alg(step) for step in initialization_sequence])

    print(result)

if __name__ == "__main__":
    main()