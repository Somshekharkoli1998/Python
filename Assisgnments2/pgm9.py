lines = []

while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line:
        lines.append(line)
    else:
        break

for line in lines:
    print(line.upper())
