
def get_sequences(history):
    sequences = [history]
    
    cur = history
    
    while not all([val == 0 for val in sequences[-1]]):        
        differences = [cur[i]-cur[i-1] for i in range(1, len(cur))]
        
        cur = differences
        
        sequences.append(differences)
    
    for i, seq in enumerate(sequences):
        print("  " * i, end="")
        for val in seq:
            print(f"{val:<4}", end="")
        print()
        
    return sequences

def extrapolate(sequences):
    result = 0
    
    for back in [seq[-1] for seq in reversed(sequences)]:
        result += back
    
    return result

def extrapolate_backwards(sequences):
    result = 0
    
    for front in [seq[0] for seq in reversed(sequences)]:
        result = front - result
    
    return result

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        history_list = [[int(val) for val in line.split()] for line in f]

    result = 0
    for history in history_list:
        ret = extrapolate_backwards(get_sequences(history))
        
        print(ret)

        result += ret
    
    print(result)

if __name__ == "__main__":
    main()