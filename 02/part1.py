
COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_line(line: str):
    game = [game_set.split(", ") for game_set in line.strip().split(": ")[1].split("; ")]
    
    for i, game_set in enumerate(game):
        game[i] = {color.split()[1]: int(color.split()[0]) for color in game_set}
    
    return game

def is_possible(game):
    possible = True
    for game_set in game:
        for color in COLORS:
            try:
                if game_set[color] > COLORS[color]:
                    possible = False
                    break
            except KeyError:
                pass
        if not possible:
            break
    
    return possible

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME) as f:
        games = [parse_line(line) for line in f]

    sum_id = 0
    for game_idx, game in enumerate(games):
        if is_possible(game):
            sum_id += game_idx + 1

    print(sum_id)

if __name__ == "__main__":
    main()