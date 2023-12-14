
def get_col(pattern, col_num):
    return "".join([pattern[row_num][col_num] for row_num in range(len(pattern))])

def check_row_mirror(pattern, row_num):
    mirrored = False
    offset = 1
    differences = 0
    
    # expand from row_num
    while row_num-offset >= 0 and row_num+offset-1 < len(pattern):
        mirrored = True
        
        for char_a, char_b in zip(pattern[row_num-offset], pattern[row_num+offset-1]):
            if char_a != char_b:
                differences += 1
            
            if differences > 1:
                mirrored = False
                break
        
        if not mirrored or differences > 1:
            break
        
        offset += 1
    
    return mirrored and differences == 1

def check_col_mirror(pattern, col_num):
    mirrored = False
    offset = 1
    differences = 0
    
    # expand from col_num
    while col_num-offset >= 0 and col_num+offset-1 < len(pattern[0]):
        mirrored = True
        
        for char_a, char_b in zip(get_col(pattern, col_num-offset), get_col(pattern, col_num+offset-1)):
            if char_a != char_b:
                differences += 1
            
            if differences > 1:
                mirrored = False
                break
        
        if not mirrored or differences > 1:
            break
        
        offset += 1
    
    return mirrored and differences == 1

def find_mirror_line(pattern):
    for row_num in range(len(pattern)):
        ret = check_row_mirror(pattern, row_num)
        if ret:
            return True, row_num
        
    for col_num in range(len(pattern[0])):
        ret = check_col_mirror(pattern, col_num)
        if ret:
            return False, col_num

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        patterns = [[line.strip() for line in pattern.strip().split("\n")] for pattern in f.read().split("\n\n")]
        
    result = 0
    for pattern in patterns:
        mult, ret = find_mirror_line(pattern)
        
        if mult:
            pattern.insert(ret, "*"*len(pattern[0]))
        else:
            for row_num, row in enumerate(pattern):
                pattern[row_num] = row[:ret] + "*" + row[ret:]
        
        for line in pattern:
            print(line)
        print(ret, "\n")
        
        result += ret * (100 if mult else 1)
    print(result)
    
if __name__ == "__main__":
    main()