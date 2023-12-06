
def parse_line(line: str):
    game = [game_set.split(", ") for game_set in line.strip().split(": ")[1].split("; ")]
    
    for i, game_set in enumerate(game):
        game[i] = {color.split()[1]: int(color.split()[0]) for color in game_set}
    
    return game

def min_possible(game):
    min_colors = {}
    for game_set in game:
        for color, amount in game_set.items():
            try:
                min_colors[color] = max(min_colors[color], amount)    
            except KeyError:
                min_colors[color] = amount
    
    return min_colors

def power(cube_set):
    product = 1
    for amount in cube_set.values():
        product *= amount
    return product

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME) as f:
        games = [parse_line(line) for line in f]

    sum_powers = 0
    for game in games:
        sum_powers += power(min_possible(game))
        
    print(sum_powers)

if __name__ == "__main__":
    main()