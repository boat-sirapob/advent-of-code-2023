
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
        
    def process_instructions(self, start="A", end="Z"):
        i = 0
        
        cur = self.get_all_ending_in(start)
        
        start_1 = [cur[0]]
        
        # while not self.are_all_ending_in(cur, end):
        while cur[0] not in start_1 or self.steps == 0:
            instruction = self.instructions[i]
            
            start_1.append(cur[0])
            
            print(cur[0], instruction, self.steps)
            
            for j, node in enumerate(cur):
                if instruction == "L":
                    cur[j] = self.nodes[node].left
                if instruction == "R":
                    cur[j] = self.nodes[node].right
                
            self.steps += 1
            
            i = (i + 1) % len(self.instructions)

        print(cur[0], instruction, self.steps)        
            
        return self.steps
    
    def get_all_ending_in(self, ending):
        return [node for node in self.nodes if node[-1] == ending]

    def are_all_ending_in(self, cur, ending):
        return all([node[-1] == ending for node in cur])

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