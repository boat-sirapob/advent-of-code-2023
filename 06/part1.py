
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
        times = [int(val) for val in f.readline().strip().split("Time:")[1].split()]
        distances = [int(val) for val in f.readline().strip().split("Distance:")[1].split()]

    result = 1
    for time, distance in zip(times, distances):
        ret = get_ways_to_beat_record(time, distance)

        # print(ret)
        
        result *= ret
        
    print(result)

if __name__ == "__main__":
    main()