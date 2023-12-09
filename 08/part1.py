
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"{self.left}, {self.right}"

class System:
    def __init__(self, instructions, nodes):
        self.instructions = instructions
        self.nodes = nodes
        self.steps = 0
        
    def process_instructions(self, start="AAA", end="ZZZ"):
        i = 0
        
        cur = start
        
        while cur != end:
            instruction = self.instructions[i]

            if instruction == "L":
                cur = self.nodes[cur].left
            if instruction == "R":
                cur = self.nodes[cur].right
                
            self.steps += 1
            
            i = (i + 1) % len(self.instructions)
            
        return self.steps

def parse_lines(lines: list[str]):
    nodes = {}
    for line in lines:
        node, next = line.strip().split(" = ")
        next = next[1:-1].split(", ")
        
        nodes[node] = Node(*next)
    
    return nodes

def main():
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        instructions = f.readline().strip()
        
        f.readline()
        
        nodes = parse_lines(f.readlines())

    s = System(instructions, nodes)
    
    ret = s.process_instructions()

    print(ret)

if __name__ == "__main__":
    main()