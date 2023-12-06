
def process_mapping(mapping, initial):
    for destination_start, source_start, range_length in mapping:
        # print(source_start, source_start + range_length, destination_start)
        if initial in range(source_start, source_start + range_length):
            return destination_start + (initial - source_start)

    return initial

def process_mappings(mappings, initial):
    cur = initial
    for mapping in mappings:
        # print(cur)
        cur = process_mapping(mapping, cur)
    return cur

def parse_seeds(line: str):
    seed_ranges = [int(val) for val in line.strip().split("seeds: ")[1].split()]

    seeds = []
    
    for i in range(0, len(seed_ranges), 2):
        for seed in range(seed_ranges[i], seed_ranges[i]+seed_ranges[i+1]):
            seeds.append(seed)

    return seeds

def parse_mapping(mapping: str):
    return [[int(val) for val in range.split()] for range in mapping.strip().split("\n")[1:]]

def main():
    FILENAME = "input.txt"
    with open(FILENAME) as f:
        seeds = parse_seeds(f.readline())
        
        print("done")
        
        mappings = [parse_mapping(mapping) for mapping in f.read().split("\n\n")]
        
    print(min([process_mappings(mappings, seed) for seed in seeds]))

if __name__ == "__main__":
    main()