import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

part1_res = 0

for line in lines:
    tens = max([int(x) for x in line[:-1]])
    ones = max(int(x) for x in line.split(str(tens), 1)[1])
    part1_res += (tens*10) + ones

part2_res = 0

for line in lines:
    res = 0
    for i in range (0,12):
        res *= 10
        if ( i == 11):
            val = max([int(x) for x in line])
        else:
            val = max([int(x) for x in line[:-(11 - i)]])
        res += val
        line = line.split(str(val), 1)[1]
    part2_res += res

print(part1_res)
print(part2_res)