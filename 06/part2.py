
def get_ways_to_beat_record(time, target_distance):
    count = 0
    
    for hold_time in range(time+1):
        speed = hold_time
        remaining_time = time - hold_time
        
        distance_travelled = speed * remaining_time
        
        if distance_travelled > target_distance:
            count += 1
        
    return count

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME) as f:
        time = int("".join(f.readline().strip().split("Time:")[1].split()))
        distance = int("".join(f.readline().strip().split("Distance:")[1].split()))

    ret = get_ways_to_beat_record(time, distance)

    print(ret)

if __name__ == "__main__":
    main()