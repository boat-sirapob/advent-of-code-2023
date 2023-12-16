
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
    north: Vector2 = Vector2( 0,-1)
    south: Vector2 = Vector2( 0, 1)
    east:  Vector2 = Vector2( 1, 0)
    west:  Vector2 = Vector2(-1, 0)
    
class RockType:
    ROUND_ROCK = "O"
    CUBE_ROCK = "#"
    EMPTY_SPACE = "."

class Platform:
    def __init__(self, platform):
        self.platform = platform
    
    def in_range(self, position):
        return 0 <= position.x < len(self.platform[0]) and 0 <= position.y < len(self.platform)
    
    def move_rock(self, start_pos, direction):
        next_pos = start_pos + direction
        
        while self.in_range(next_pos) and self.platform[next_pos.y][next_pos.x] == ".":        
            self.platform[next_pos.y][next_pos.x], self.platform[start_pos.y][start_pos.x] = self.platform[start_pos.y][start_pos.x], self.platform[next_pos.y][next_pos.x]
            next_pos = next_pos + direction

    def tilt(self, direction):
        state = [[char for char in line] for line in self.platform]
        new_state = None
        while state != new_state:
            round_rocks = self.get_rock_positions(RockType.ROUND_ROCK)
            if new_state:
                state = new_state
            for pos in round_rocks:
                self.move_rock(pos, direction)
            new_state = [[char for char in line] for line in self.platform]
            
    def get_load(self):
        return sum([row.count(RockType.ROUND_ROCK) * (len(self.platform) - row_num) for row_num, row in enumerate(self.platform)])

    def get_rock_positions(self, rock_type: RockType):
        positions = []
        
        for y, row in enumerate(self.platform):
            for x, cell in enumerate(row):
                if cell == rock_type:
                    positions.append(Vector2(x, y))
        
        return positions
    
    def spin_cycle(self, n=1):
        # this loops at some point so just find
        # (n - leadin) % loop length == (cur iteration in loop) and break
        # or calculate index from cache
        states = {}
        
        for i in range(n):
            if i % 1000 == 0:
                print(i)
            self.tilt(Direction.north)
            self.tilt(Direction.west)
            self.tilt(Direction.south)
            self.tilt(Direction.east)
            
            cur_state = tuple(["".join(line) for line in self.platform])
        
            if cur_state in states:
                loop_length = i - states[cur_state]
                print(f"Loop length: {loop_length}")
                print(f"Lead in: {len(states) - loop_length}")
                print(f"len(states): {len(states)}")
                break
                
            states[cur_state] = i
            
    def display(self):
        for line in self.platform:
            for cell in line:
                print(cell, end="")
            print()

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        platform = [[char for char in line.strip()] for line in f]
    
    p = Platform(platform)
    
    print(platform)
    
    p.display()
    print()
    
    p.spin_cycle(1000000000)
    
    p.display()
    
    ret = p.get_load()
    
    print(ret)
    
if __name__ == "__main__":
    main()