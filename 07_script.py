from collections import defaultdict
from itertools import accumulate


INPUT_FILE = "in.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as file:
        sys = defaultdict(int)
        curr = ['/']
        for line in file:
            line=line[:-1]
            match (line.split(' ')):
                case '$', 'cd', '/':
                    curr = ['/']
                case '$', 'cd', '..':
                    curr.pop()
                case '$', 'cd', directory:
                    curr.append(directory+'/')
                case '$', 'ls':
                    pass
                case 'dir', _:
                    pass
                case size, name:
                    for path in accumulate(curr):
                        sys[path] += int(size)

        # min 
        sizes = sys.values()
        print(
            sum([s for s in sizes if s <= 100_000]), # 1423358
        )
        print(" ")
        minimum_delete = 30_000_000 - (70_000_000 - sys['/'])
        print(min([s for s in sizes if s >= minimum_delete]))