import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append([x for x in line.rstrip()])

# splits = 0

# for i in range(1, len(lines)):
#     for j in range(len(lines[i])):
#         if lines[i-1][j] == 'S':
#             lines[i][j] = '|'
#         elif lines[i-1][j] == '|' and lines[i][j] == '^':
#             splits += 1
#             if j > 0 and lines[i][j-1] == '.':
#                 lines[i][j-1] = '|'
#             if j < len(lines[i]) - 1 and lines[i][j+1] == '.':
#                 lines[i][j+1] = '|'
#         elif lines[i-1][j] == '|':
#             lines[i][j] = '|'

# for line in lines:
#     print("".join(line))

# print(splits)

for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        
        if lines[i-1][j] == 'S':
            lines[i][j] = 1
        
        elif isinstance(lines[i-1][j], int) and lines[i][j] == '^':
            if j > 0:
                if isinstance(lines[i][j-1], int):
                    lines[i][j-1] = lines[i][j-1] + lines[i-1][j]
                elif lines[i][j-1] == '.':
                    lines[i][j-1] = lines[i-1][j]

            if j < len(lines[i]) - 1 and lines[i][j+1] == '.':
                lines[i][j+1] = lines[i-1][j]
        
        elif isinstance(lines[i-1][j], int):
            if isinstance(lines[i][j], int):
                lines[i][j] = lines[i][j] + lines[i-1][j]
            else:
                lines[i][j] = lines[i-1][j]

print(sum(x for x in lines[-1] if isinstance(x, int)))