import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

for i in range(len(lines)):
    lines[i] = [c for c in lines[i]]

total = 0

accessible = -1

while (accessible != 0):
    accessible = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j] == '@'):
                # need at least 5 open spaces
                rolls = 0

                # up left
                if i > 0 and j > 0 and lines[i-1][j-1] == '@':
                    rolls += 1

                # up
                if i > 0 and lines[i-1][j] == '@':
                    rolls += 1

                # up right
                if i > 0 and j < len(lines[i]) - 1 and lines[i-1][j+1] == '@':
                    rolls += 1

                # left
                if j > 0 and lines[i][j-1] == '@':
                    rolls += 1

                # right
                if j < len(lines[i]) - 1 and lines[i][j+1] == '@':
                    rolls += 1

                # bottom left
                if j > 0 and i < len(lines) - 1 and lines[i+1][j-1] == '@':
                    rolls += 1

                # bottom
                if i < len(lines) - 1 and lines[i+1][j] == '@':
                    rolls += 1

                # bottom right
                if i < len(lines) - 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == '@':
                    rolls += 1

                if rolls < 4:
                    lines[i][j] = '.'
                    accessible += 1
    total += accessible

print(total)

