with open("../data/notes.txt") as f:
    line_number = 1
    for line in f:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1
