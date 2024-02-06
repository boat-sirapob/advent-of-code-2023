
display_pipes = {
    "|": "┃",
    "-": "━",
    "L": "┗",
    "J": "┛",
    "7": "┓",
    "F": "┏",
    ".": ".",
    "S": "S",
}

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

directions = {
    "right": Vector2( 1, 0),
    "left": Vector2(-1, 0),
    "down": Vector2( 0, 1),
    "up": Vector2( 0,-1)
}

class PipeSystem:
    def __init__(self, pipes):
        self.pipes = pipes
        self.start = self.get_starting_pos()
        self.loop = {(pos.x, pos.y) for pos in self.get_loop()}
    
    def at(self, vector2_or_x, y = None):
        if y is not None:
            return self.pipes[y][vector2_or_x]
        return self.pipes[vector2_or_x.y][vector2_or_x.x]

    def get_starting_pos(self):
        for y in range(len(self.pipes)):
            for x in range(len(self.pipes[y])):
                if self.at(x, y) == "S":
                    return Vector2(x, y)
        return None

    def are_connected(self, pos1: Vector2, pos2: Vector2):
        if pos2.y == pos1.y-1:
            return self.at(pos1) in ["|","L","J","S"] and self.at(pos2) in ["|","7","F","S"]
        if pos2.y == pos1.y+1:
            return self.at(pos1) in ["|","7","F","S"] and self.at(pos2) in ["|","L","J","S"]
        if pos2.x == pos1.x-1:
            return self.at(pos1) in ["-","J","7","S"] and self.at(pos2) in ["-","L","F","S"]
        if pos2.x == pos1.x+1:
            return self.at(pos1) in ["-","L","F","S"] and self.at(pos2) in ["-","J","7","S"]

    def get_connected_neighbors(self, pos: Vector2):
        
        neighbors = [pos + direction for direction in directions.values() if self.are_connected(pos, pos + direction)]

        return neighbors

    def get_loop(self):
        start = self.start
        end = self.get_connected_neighbors(start)[0]
        
        stack = [start]
        loop = set()
        
        while len(stack) != 0:
            
            cur = stack.pop()

            loop.add(cur)
            
            if cur == end:
                return loop

            for neighbor in self.get_connected_neighbors(cur):
                if neighbor in loop:
                    continue

                stack.append(neighbor)

        raise RuntimeError("Could not find loop from starting position")

    def get_steps_to_farthest(self):
        start = self.start
        
        queue = [start]
        distances = [0]
        visited = set()
        
        farthest = 0
        
        while len(queue) != 0:
            
            cur = queue.pop(0)
            farthest = distances.pop(0)

            visited.add(cur)
            
            for neighbor in self.get_connected_neighbors(cur):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                distances.append(farthest + 1)
        
        return farthest

    def display(self):
        for line in self.pipes:
            for char in line:
                print(display_pipes[char], end="")
            print()
            
    def display_loop(self):
        enclosed = self.get_enclosed()

        for y, line in enumerate(self.pipes):
            for x, char in enumerate(line):
                display_char = display_pipes["."]
                if (x, y) in self.loop:
                    display_char = display_pipes[char]
                if (x, y) in enclosed:
                    display_char = "*"
                print(display_char, end="")
            print()
            
    def is_inside_loop(self, x, y):
        # look up or down, whichever is closer, and count number of vertical pipes
        # if odd, inside; else, outside
        
        step = 1 if y > len(self.pipes)//2 else -1

        cur_y = y

        temp = []
        count = 0
        while 0 <= cur_y < len(self.pipes):
            if (x, cur_y) in self.loop and self.at(x, cur_y) in ["-", "J","7"]:
                count += 1
                temp.append((x, cur_y))
            cur_y += step
            
        if count % 2 == 1:
            print(x, y, count, temp)
        
        return count % 2 == 1

    def get_enclosed(self):        
        self.replace_start()
        
        enclosed = set()
        for y, line in enumerate(self.pipes):
            for x, char in enumerate(line):
                if (x, y) not in self.loop:
                    if self.is_inside_loop(x, y):
                        enclosed.add((x, y))             
        return enclosed

    def count_enclosed(self):
        return len(self.get_enclosed())
    
    def in_range(self, x, y):
        return 0 <= x < len(self.pipes[y]) and 0 <= y < len(self.pipes)
    
    def replace_start(self):
        replacements = {
            ("up", "down"): "|",
            ("left", "right"): "-",
            ("up", "right"): "L",
            ("up", "left"): "J",
            ("down", "left"): "7",
            ("down", "right"): "F"
        }
        
        start = self.start
        
        if not start:
            return
        
        connects = []
        for dir, dvec in directions.items():
            if self.are_connected(start, start+dvec):
                connects.append(dir)
        
        line = self.pipes[start.y]
        for c, r in replacements.items():
            if c[0] in connects and c[1] in connects:
                self.pipes[start.y] = line[:start.x] + r + line[start.x+1:]
                break

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        pipes = [line.strip() for line in f]
    
    s = PipeSystem(pipes)

    print(s.get_steps_to_farthest())
    
    s.display_loop()
    
    print(s.count_enclosed())
    
if __name__ == "__main__":
    main()