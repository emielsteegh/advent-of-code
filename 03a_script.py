
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_priority(ch):
    return priority.index(ch)+1

def calc_backpack_priority(content):
    backpack_size = len(content)
    half_backpack = int(backpack_size/2) # always divisible by 2

    comp_a = set(content[:half_backpack])
    comp_b = set(content[half_backpack:])
    intersect = comp_a.intersection(comp_b)

    backpack_priority = 0
    for ch in intersect:
        backpack_priority += get_priority(ch)
    
    return backpack_priority

INPUT_FILE = "in.txt"
if __name__ == "__main__":
    total_priority = 0
    with open(INPUT_FILE) as f:
        for line in f:
            line = line[:-1] # remove newline >:(
            total_priority += calc_backpack_priority(line)
    
    print(total_priority)
