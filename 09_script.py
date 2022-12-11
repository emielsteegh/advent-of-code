import numpy as np

def move(d, steps, rope, v): 
    match d:
        case 'U': d = [-1,0]
        case 'D': d = [1,0]
        case 'L': d = [0,-1]
        case 'R': d = [0,1]
    
    for _ in range(int(steps)):
        rope[0] += d # move head
        for seg in range(1,len(rope)):
            delta = rope[seg-1] - rope[seg] # difference from segment to one ahead

            if np.abs(delta).max() >= 2: # no longer touching
                rope[seg] += np.clip(delta,-1,1) # clip to make max step in any 4-dir one
                if seg == len(rope)-1: # check if the tail end moved
                    v.add(tuple(rope[seg]))
            else:
                break # part did not move, it's tail wont either

    return rope, v
    

INPUT_FILE = "in.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as file:
        rope = [np.array([0,0]) for _ in range(10)]
        v = {tuple(rope[8])} # visited
        for line in file:
            line=line[:-1]
            rope, v = move(*line.split(" "), rope=rope, v=v)
        print(f"tail visited: {len(v)}")