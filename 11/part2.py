    
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"({self.x}, {self.y})"

class GalaxyImage:
    EXPANSION_MULTIPLIER = 1_000_000
    
    def __init__(self, image):
        self.image: list[str] = image
        self.empty_row_tracker = {}
        self.empty_col_tracker = {}
        
        self.populate_empty_trackers()
        
    def populate_empty_trackers(self):
        self.empty_row_tracker[0] = self.empty_rows(0,0)
        for y in range(1, len(self.image)):
            self.empty_row_tracker[y] = self.empty_row_tracker[y-1] + self.empty_rows(y, y)
        
        self.empty_col_tracker[0] = self.empty_cols(0,0)
        for x in range(1, len(self.image[0])):
            self.empty_col_tracker[x] = self.empty_col_tracker[x-1] +  self.empty_cols(x, x)
    
    def empty_rows(self, start_row, end_row):
        result = 0
        for row_num in range(start_row, end_row+1):
            row = self.image[row_num]
            result += all([cell == "." for cell in row])
        return result
        
    def empty_cols(self, start_col, end_col):
        result = 0
        for col_num in range(start_col, end_col+1):
            result += all([self.image[i][col_num] == "." for i in range(len(self.image))])
        return result
    
    def get_galaxy_positions(self):
        positions = []
        
        for y, row in enumerate(self.image):
            for x, cell in enumerate(row):
                if cell == "#":
                    positions.append(Vector2(x, y))
                    
        return positions
    
    def steps_shortest_path(self, start: Vector2, end: Vector2):
        empty_rows = self.empty_row_tracker[end.y] - self.empty_row_tracker[start.y]
        empty_cols = self.empty_col_tracker[end.x] - self.empty_col_tracker[start.x]
        
        return (
            abs(end.x-start.x) + abs(empty_rows)*(GalaxyImage.EXPANSION_MULTIPLIER-1)
          + abs(end.y-start.y) + abs(empty_cols)*(GalaxyImage.EXPANSION_MULTIPLIER-1)
        )
    
    def display(self):
        for row in self.image:
            print(row)

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        image = [line.strip() for line in f]
        
    g = GalaxyImage(image)
    
    galaxies = g.get_galaxy_positions()

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            result += g.steps_shortest_path(galaxies[i], galaxies[j])
    print(result)
        
if __name__ == "__main__":
    main()