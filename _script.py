import numpy as np

INPUT_FILE = "in.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as f:
        for line in f:
            line=line[:-1]
