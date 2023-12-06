import string

class Schematic:
    def __init__(self, grid):
        self.grid = grid
        self.visited = []
    
    def at(self, x, y):
        return self.grid[y][x]
    
    def get_symbol_coords(self):
        symbol_coords = [] # (x, y)
    
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != "." and self.grid[row][col] in string.punctuation:
                    symbol_coords.append((col, row))

        return symbol_coords
    
    def get_part_numbers(self):
        part_numbers = []
        
        symbol_coords = self.get_symbol_coords()
        for coord in symbol_coords:
            part_numbers += self.get_adjacent_part_numbers(*coord)

        return part_numbers
    
    def get_adjacent_part_numbers(self, x, y):
        part_numbers = []
        for i in range(-1,2):
            for j in range(-1,2):
                if (i, j) == (0, 0):
                    continue
                cur = (x + i, y + j)
                if cur not in self.visited and self.at(*cur) != ".":
                    ret = self.part_number_at(*cur)
                    print(ret)
                    part_numbers.append(ret)
        return part_numbers
    
    def part_number_at(self, x, y):
        left = x
        right = x
        while left > 0 and self.grid[y][left-1].isnumeric():
            left -= 1
        while right < len(self.grid[y]) and self.grid[y][right].isnumeric():
            right += 1
        
        for col in range(left, right):
            self.visited.append((col, y))
        
        return int(self.grid[y][left:right])
    
def main():
    FILENAME = "input.txt"
    
    with open(FILENAME) as f:
        grid = [line.strip() for line in f]
        
    s = Schematic(grid)
    
    ret = s.get_part_numbers()

    print(sum(ret))

if __name__ == "__main__":
    main()