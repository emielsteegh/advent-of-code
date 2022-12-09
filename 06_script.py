
INPUT_FILE = "06_input.txt"
MARKER_LEN = 14
if __name__ == "__main__":
    
    with open(INPUT_FILE) as file:
        for line in file:
            line=line[:-1]
            buffer = line[:MARKER_LEN-1]
            location = 1
            for ch in range(MARKER_LEN-1,len(line)+1):
                # print(set(buffer+line[ch]))
                if len(set(buffer+line[ch])) == MARKER_LEN:
                    print(ch+1)
                    break
                else:
                    buffer = buffer[1:] + line[ch]
                