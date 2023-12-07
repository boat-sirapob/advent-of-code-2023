from functools import cmp_to_key

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_ranks = {c: rank for rank, c in enumerate(cards)}

hand_types = [
    "five of a kind",
    "four of a kind",
    "full house",
    "three of a kind",
    "two pair",
    "one pair",
    "high card",
]
hand_types_ranks = {hand: rank for rank, hand in enumerate(hand_types)}

def evaluate_hand(hand: str):
    counts = {}
    
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
        
    # handle joker
    if "J" in counts:
        counts_without_j = {card: counts[card] for card in counts if card != "J"}
        
        if counts_without_j:
            # get the card with the highest count that isn't J
            highest_count_card = max(counts_without_j, key=lambda card: counts[card])
            
            counts[highest_count_card] += counts["J"]
            counts["J"] = 0
    
    count_values = list(counts.values())
    
    if 5 in count_values:
        return hand_types_ranks["five of a kind"]
    if 4 in count_values:
        return hand_types_ranks["four of a kind"]
    if 3 in count_values and 2 in count_values:
        return hand_types_ranks["full house"]
    if 3 in count_values:
        return hand_types_ranks["three of a kind"]
    if count_values.count(2) == 2:
        return hand_types_ranks["two pair"]
    if 2 in count_values:
        return hand_types_ranks["one pair"]
    return hand_types_ranks["high card"]

def compare_hands(hand_a, hand_b):
    if (eval_a := evaluate_hand(hand_a)) != (eval_b := evaluate_hand(hand_b)):
        return 1 if eval_a < eval_b else -1
    
    for card_a, card_b in zip(hand_a, hand_b):
        rank_a = card_ranks[card_a]
        rank_b = card_ranks[card_b]
        
        if rank_a == rank_b:
            continue
        
        return 1 if rank_a < rank_b else -1
    
    return 0

def get_total_winnings(hands):
    ranked_hands = sorted(hands, key=lambda hand: cmp_to_key(compare_hands)(hand[0]))    

    total_winnings = 0
    for rank, (_, bid) in enumerate(ranked_hands):
        total_winnings += (rank+1) * bid
    
    return total_winnings

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        hands = [line.strip().split() for line in f]
        hands = [[hand, int(bid)] for hand, bid in hands]

    ret = get_total_winnings(hands)
    
    print(ret)

if __name__ == "__main__":
    main()