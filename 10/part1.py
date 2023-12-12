
display_pipes = {
    "|": "┃",
    "-": "━",
    "L": "┗",
    "J": "┛",
    "7": "┓",
    "F": "┏",
    ".": " ",
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

class PipeSystem:
    def __init__(self, pipes):
        self.pipes = pipes
    
    def at(self, vector2_or_x, y = None):
        if y is not None:
            return self.pipes[y][vector2_or_x]
        return self.pipes[vector2_or_x.y][vector2_or_x.x]

    def get_starting_pos(self):
        for y in range(len(self.pipes)):
            for x in range(len(self.pipes[y])):
                if self.at(x, y) == "S":
                    return Vector2(x, y)
        raise RuntimeError("Could not find starting position")

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
        directions = [
            Vector2( 1, 0),
            Vector2(-1, 0),
            Vector2( 0, 1),
            Vector2( 0,-1)
        ]
        neighbors = [pos + direction for direction in directions if self.are_connected(pos, pos + direction)]

        return neighbors

    def get_loop(self):
        start = self.get_starting_pos()
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
        start = self.get_starting_pos()
        
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
        loop = {(pos.x, pos.y) for pos in self.get_loop()}
        
        for y, line in enumerate(self.pipes):
            for x, char in enumerate(line):
                display_char = " "
                if (x, y) in loop:
                    display_char = display_pipes[char]
                print(display_char, end="")
            print()

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        pipes = [line.strip() for line in f]
    
    s = PipeSystem(pipes)

    s.display_loop()
    
    print(s.get_steps_to_farthest())
    
if __name__ == "__main__":
    main()