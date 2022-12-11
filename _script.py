import numpy as np

INPUT_FILE = "in.txt"
if __name__ == "__main__":
    
    with open(INPUT_FILE) as file:
        for line in file:
            line=line[:-1]
