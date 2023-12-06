
def get_ways_to_beat_record(time, target_distance):
    return int((time**2 - 4*target_distance) ** 0.5)

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME) as f:
        time = int("".join(f.readline().strip().split("Time:")[1].split()))
        distance = int("".join(f.readline().strip().split("Distance:")[1].split()))

    ret = get_ways_to_beat_record(time, distance)

    print(ret)

if __name__ == "__main__":
    main()