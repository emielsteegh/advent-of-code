CARGO= """    [B]             [B] [S]        
    [M]             [P] [L] [B] [J]
    [D]     [R]     [V] [D] [Q] [D]
    [T] [R] [Z]     [H] [H] [G] [C]
    [P] [W] [J] [B] [J] [F] [J] [S]
[N] [S] [Z] [V] [M] [N] [Z] [F] [M]
[W] [Z] [H] [D] [H] [G] [Q] [S] [W]
[B] [L] [Q] [W] [S] [L] [J] [W] [Z]
 1   2   3   4   5   6   7   8   9 """

def cargo_to_stacks(cargo):
    # turns the cargo code into neat dicts
    cargo = cargo.split('\n')
    cargo.reverse()
    stacks = {}
    current_stack = 0
    for i in range(1,len(cargo[0]),4):
        for line in cargo:
            if line[i].isnumeric(): 
                current_stack = line[i]
                stacks[current_stack] = []
            elif line[i] != ' ':
                stacks[current_stack].append(line[i])
    return stacks

def move_stacks(stacks, count, fro, to, reverse):
    move = []
    for p in range(int(count)):
        move.append(stacks[fro].pop()) #this reverses the order of picked up crates
    
    if reverse:
        stacks[to].extend(move)
    else:
        stacks[to].extend(move[::-1]) # "un"reverse
    return(stacks)


INPUT_FILE = "input/05.txt"
if __name__ == "__main__":
    
    part1 = cargo_to_stacks(CARGO)
    part2 = cargo_to_stacks(CARGO)

    with open(INPUT_FILE) as f:
        for line in f:
            line=line[:-1]
            comm = line.split(" ")
            part1 = move_stacks(part1, comm[1], comm[3], comm[5], reverse=True)
            part2 = move_stacks(part2, comm[1], comm[3], comm[5], reverse=False)
    
    tops = lambda x: print("".join([s[-1] for s in x.values()]))
    tops(part1)
    tops(part2)
