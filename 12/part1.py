
def is_valid(spring_conditions, orig_group_sizes: list[int]):
    group_idx = 0
    cur_group_size = 0

    for char in spring_conditions + ".":
        if char == "#":
            # invalid if current group larger than corresponding group size
            cur_group_size += 1
            if group_idx >= len(orig_group_sizes) or cur_group_size > orig_group_sizes[group_idx]:
                return False
        elif cur_group_size > 0:
            # invalid if end of group and group size not equal to corresponding group size
            if cur_group_size != orig_group_sizes[group_idx]:
                return False
            cur_group_size = 0
            group_idx += 1
        
    return group_idx == len(orig_group_sizes)

def get_arrangements(spring_conditions, group_sizes):
    
    # print(spring_conditions)
    
    try:
        question_mark_idx = spring_conditions.index("?")
        
        return (
            get_arrangements(spring_conditions[:question_mark_idx]+"."+spring_conditions[question_mark_idx+1:], group_sizes) 
          + get_arrangements(spring_conditions[:question_mark_idx]+"#"+spring_conditions[question_mark_idx+1:], group_sizes)
        )
        
    except ValueError:
        # if is_valid(spring_conditions, group_sizes):
        #     return [spring_conditions]
        # else:
        #     return []

        return int(is_valid(spring_conditions, group_sizes))

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        records = [line.strip().split() for line in f]
        for r in records:
            r[1] = [int(val) for val in r[1].split(",")]
        
    result = 0
    for r in records:
        ret = get_arrangements(*r)
        result += ret
        
    print(result)
    
if __name__ == "__main__":
    main()