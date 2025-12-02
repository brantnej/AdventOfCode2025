import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

invalid_ids = set()

for i in range(0, 5):
    # i = number of zeros in between 1's places
    # i = exponent of 10 to check
    multipliers = []
    base_mult = (10**(i+1))
    current_mult = base_mult + 1

    # can just use current_mult for part 1
    for j in range(0,10-(2*i)):
        multipliers.append(current_mult)
        current_mult *= base_mult
        current_mult += 1
    for j in range(10**i, 10**(i+1)):
        for mult in multipliers:
            invalid_ids.add(j*mult)
    
ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in lines[0].split(',')]

res = 0

for r in ranges:
    for i in range(r[0], r[1] + 1):
        if i in invalid_ids:
            res += i

print(res)