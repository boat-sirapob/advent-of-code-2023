
def get_card_points(card):
    winning_numbers, card_numbers = card
    
    points = 0
    for num in card_numbers:
        if num in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    
    return points

def parse_line(line: str):
    card = [[int(num) for num in num_list.split()] for num_list in line.strip().split(": ")[1].split(" | ")]

    return card

def main():
    FILENAME = "input.txt"
    with open(FILENAME) as f:
        cards = [parse_line(line) for line in f]
        
    print(sum([get_card_points(card) for card in cards]))

if __name__ == "__main__":
    main()