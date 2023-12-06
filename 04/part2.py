
def process_card(card, card_num, num_cards):
    winning_numbers, card_numbers = card
    
    offset = 1
    for num in card_numbers:
        if num in winning_numbers:
            num_cards[card_num + offset] += num_cards[card_num]
            offset += 1

def parse_line(line: str):
    card = [[int(num) for num in num_list.split()] for num_list in line.strip().split(": ")[1].split(" | ")]

    return card

def main():
    FILENAME = "input.txt"
    with open(FILENAME) as f:
        cards = [parse_line(line) for line in f]
        num_cards = [1 for _ in range(len(cards))]
    
    for card_num, card in enumerate(cards):
        process_card(card, card_num, num_cards)

    print(sum(num_cards))
    
if __name__ == "__main__":
    main()