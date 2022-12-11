import numpy as np

def move(d, steps, h, t, v): 
    match d:
        case 'U': d = [-1,0]
        case 'D': d = [1,0]
        case 'L': d = [0,-1]
        case 'R': d = [0,1]
    
    for _ in range(int(steps)):
        h += d # move head
        delta = h - t # difference from tail to head

        if np.abs(delta).max() >= 2: # no longer touching
            t += np.clip(delta,-1,1) # clip to make max step in any 4-dir one
            v.add(tuple(t)) # add new tail location to visited

    return h, t, v
    

INPUT_FILE = "09_input.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as file:
        h = np.array([0,0]) # location head
        t = np.array([0,0]) # location tail
        v = {tuple(t)} # visited
        for line in file:
            line=line[:-1]
            h, t, v = move(*line.split(" "), h=h, t=t, v=v)
        print(f"head {tuple(h)}\ntail {tuple(t)}\ntail visited: {len(v)}")