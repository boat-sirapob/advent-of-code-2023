
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other: "Vector2"):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __eq__(self, other: "Vector2"):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class GalaxyImage:
    def __init__(self, image):
        self.image: list[str] = image
    
    def expand_row(self, row_num):
        row = self.image[row_num]
        self.image.insert(row_num, "."*len(row))
        
    def expand_col(self, col_num):
        for i, row in enumerate(self.image):
            self.image[i] = row[:col_num] + "." + row[col_num:]
        
    def expand_empty(self):
        # go through rows
        for row_num in range(len(self.image)-1,-1,-1):
            row = self.image[row_num]
            if all([cell == "." for cell in row]):
                self.expand_row(row_num)
        
        # go through cols
        for col_num in range(len(self.image[0])-1,-1,-1):
            if all([self.image[i][col_num] == "." for i in range(len(self.image))]):
                self.expand_col(col_num)
    
    def get_galaxy_positions(self):
        positions = []
        
        for y, row in enumerate(self.image):
            for x, cell in enumerate(row):
                if cell == "#":
                    positions.append(Vector2(x, y))
                    
        return positions
    
    def steps_shortest_path(self, start: Vector2, end: Vector2):
        return abs(end.x - start.x) + abs(end.y - start.y)
    
    def display(self):
        for row in self.image:
            print(row)

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        image = [line.strip() for line in f]
        
    g = GalaxyImage(image)
    
    g.expand_empty()
    # g.display()

    galaxies = g.get_galaxy_positions()

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            result += g.steps_shortest_path(galaxies[i], galaxies[j])
    
    print(result)
    
if __name__ == "__main__":
    main()