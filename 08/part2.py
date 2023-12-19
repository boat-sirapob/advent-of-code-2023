
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
        
        states = [[] for _ in range(len(cur))]
        
        loop_lengths = [None for _ in range(len(cur))]
        
        while not all(loop_lengths):
            instruction = self.instructions[i]
            
            for j, node in enumerate(cur):
                # get loop length when state repeats and skip
                if node[-1] == end:
                    try:
                        state_index = states[j].index(node)

                        if loop_lengths[j] == None:
                            loop_lengths[j] = self.steps - state_index
                        continue
                    except ValueError:
                        pass                
                
                states[j].append(node)
                
                if instruction == "L":
                    cur[j] = self.nodes[node].left
                if instruction == "R":
                    cur[j] = self.nodes[node].right
                
            self.steps += 1
            
            i = (i + 1) % len(self.instructions)
            
        return lcm(*loop_lengths)
    
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

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(*args):
    a = args[0]
    b = args[1:]
    if len(b) != 1:
        b = lcm(*b)
    else:
        b = b[0]
    return a*b // gcd(a,b)

def main():
    
    FILENAME = "input.txt"
    
    with open(FILENAME, "r") as f:
        instructions = f.readline().strip()
        
        f.readline()
        
        nodes = parse_lines(f.readlines())

    s = System(instructions, nodes)
    
    result = s.process_instructions()
    
    print(result)

if __name__ == "__main__":
    main()