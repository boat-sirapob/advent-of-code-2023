
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

class Direction:
    UP = Vector2(0,-1)
    DOWN = Vector2(0,1)
    LEFT = Vector2(-1,0)
    RIGHT = Vector2(1,0)

class Beam:
    def __init__(self, pos, direction):
        self.pos: Vector2 = pos
        self.direction: Direction = direction
        
    def __hash__(self):
        return hash((self.pos, self.direction))
    
    def __repr__(self):
        return f"({self.pos.x}, {self.pos.y})"
    
class Contraption:
    EMPTY_SPACE = "."
    UP_MIRROR = "/"
    DOWN_MIRROR = "\\"
    VERTICAL_SPLITTER = "|"
    HORIZONTAL_SPLITTER = "-"
    
    def __init__(self, tiles):
        self.tiles = tiles
        self.beams = [
            Beam(pos=Vector2(0,0), direction=Direction.RIGHT)
        ]
        self.energized_tiles = set()
        self.visited = set()
    
    def at(self, pos):
        return self.tiles[pos.y][pos.x]
    
    def in_range(self, pos):
        return (
            0 <= pos.y < len(self.tiles) and 0 <= pos.x < len(self.tiles[pos.y])
        )
    
    def step(self):
        to_remove = []
        for beam in self.beams:
            self.energized_tiles.add(beam.pos)
            
            self.visited.add((beam.pos, beam.direction))
            
            cur = self.at(beam.pos)
            
            if cur == Contraption.UP_MIRROR:
                if beam.direction == Direction.UP:
                    beam.direction = Direction.RIGHT
                elif beam.direction == Direction.DOWN:
                    beam.direction = Direction.LEFT
                elif beam.direction == Direction.RIGHT:
                    beam.direction = Direction.UP
                elif beam.direction == Direction.LEFT:
                    beam.direction = Direction.DOWN
            
            if cur == Contraption.DOWN_MIRROR:
                if beam.direction == Direction.UP:
                    beam.direction = Direction.LEFT
                elif beam.direction == Direction.DOWN:
                    beam.direction = Direction.RIGHT
                elif beam.direction == Direction.RIGHT:
                    beam.direction = Direction.DOWN
                elif beam.direction == Direction.LEFT:
                    beam.direction = Direction.UP
                    
            if cur == Contraption.VERTICAL_SPLITTER:
                if beam.direction not in [Direction.UP, Direction.DOWN]:
                    beam.direction = Direction.UP
                    to_add = Beam(beam.pos, Direction.DOWN)
                    self.beams.append(to_add)
            
            if cur == Contraption.HORIZONTAL_SPLITTER:
                if beam.direction not in [Direction.LEFT, Direction.RIGHT]:
                    beam.direction = Direction.LEFT
                    to_add = Beam(beam.pos, Direction.RIGHT)
                    self.beams.append(to_add)
                        
            beam.pos += beam.direction
            
            if not self.in_range(beam.pos) or (beam.pos, beam.direction) in self.visited:
                to_remove.append(beam)
                
        for beam in to_remove:
            self.beams.remove(beam)
        
    def run(self, n=0):
        i = 0
        while i < n or (n == 0 and self.beams):
            self.step()
            
            # self.display()
            
            i += 1
        
    def display(self):
        result = ""
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if Vector2(x,y) in self.energized_tiles:
                    result += "#"
                else:
                    result += tile
            result += "\n"
        print(result)

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        tiles = [line.strip() for line in f]
        
    c = Contraption(tiles)
    
    c.display()
    c.run()    
    c.display()
    print(len(c.energized_tiles))
    
if __name__ == "__main__":
    main()