INPUT_FILE = "in.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as f:
        # absolutely unintelligible solution of stacked list comprehensions
        coms = [1] + [int(i) for ll in [[0] if line[:-1] == "noop" else [0,line[:-1].split()[1]] for line in f] for i in ll]
        vals = [sum(coms[:x]) for x in range(1,len(coms))]
        print(sum([p * vals[p-1] for p in range(20,221,40)]))
        
        lines = ["█" if beam%40 - vals[beam] in [-1,0,1] else " " for beam in range(0,240)]
        [print("".join(lines[i-40:i])) for i in range(40,241,40)]