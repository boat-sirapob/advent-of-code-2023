
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

def parse_mapping(mapping: str):
    return [[int(val) for val in range.split()] for range in mapping.strip().split("\n")[1:]]

def main():
    FILENAME = "input.txt"
    with open(FILENAME) as f:
        seeds = [int(val) for val in f.readline().strip().split("seeds: ")[1].split()]
        
        mappings = [parse_mapping(mapping) for mapping in f.read().split("\n\n")]
        
    print(min([process_mappings(mappings, seed) for seed in seeds]))

if __name__ == "__main__":
    main()