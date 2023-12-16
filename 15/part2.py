
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return f"{self.key}: {self.value}"

boxes = [[] for _ in range(256)]

def hash_alg(string: str):
    cur = 0
    
    for char in string:
        ascii_code = ord(char)
        cur = ((cur + ascii_code) * 17) % 256
        
    return cur

def remove_lens(label):
    hash_val = hash_alg(label)

    box = boxes[hash_val]
    try:
        lens_to_remove = next(item for item in box if item.key == label)
        box.remove(lens_to_remove)
    except StopIteration:
        pass

def assign_lens(label, value):
    hash_val = hash_alg(label)

    box = boxes[hash_val]

    try:
        # if already exists
        lens_index = box.index(next(item for item in box if item.key == label))
        
        box[lens_index].value = value

    except StopIteration:
        box.append(Item(label, value))

def process_step(step: str):
    if step[-1] == "-":
        label = step[:-1]
        remove_lens(label)

    else:
        label, value = step.split("=")
        assign_lens(label, int(value))
        
def display_boxes():
    for box_num, box in enumerate(boxes):
        if len(box) > 0:
            print(f"Box {box_num}: {box}")

def get_total_focusing_power():
    total = 0
    for box_num, box in enumerate(boxes):
        for slot_number, lens in enumerate(box):
            total += (box_num + 1) * (slot_number + 1) * lens.value
    return total

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        initialization_sequence = f.read().strip().split(",")

    for step in initialization_sequence:
        process_step(step)

    display_boxes()
    
    ret = get_total_focusing_power()

    print(ret)
    
if __name__ == "__main__":
    main()