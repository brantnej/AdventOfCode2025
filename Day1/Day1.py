import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

pos = 50
zeroes = 0
clicks = 0

for line in lines:
    num = int(line[1:])

    old_pos = pos

    if (line[0] == 'L'):
        pos -= num
    else:
        pos += num

    if (pos <= 0):
        clicks += int(abs(pos) / 100) + 1
        if (old_pos == 0):
            clicks -= 1  
    elif (pos >= 100):
        clicks += int(pos / 100)

    pos = pos % 100

    if (pos == 0):
        zeroes += 1

print(zeroes)
print(clicks)