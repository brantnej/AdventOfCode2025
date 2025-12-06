import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append([x for x in line.rstrip()])

max_len = max([len(line) for line in lines])
for line in lines:
    while (len(line) < max_len):
        line.append(' ')

# part 1

# numbers = []

# operators = []

# for line in lines:
#     if line is not lines[len(lines) - 1]:
#         numbers.append([int(x) for x in line.split()])
#     else:
#         operators = [x for x in line.split()]

# res = 0

# for i in range(len(operators)):
#     num = numbers[0][i]
#     for j in range(1, len(numbers)):
#         if operators[i] == '+':
#             num += numbers[j][i]
#         else:
#             num *= numbers[j][i] 
#     res += num

# print(res)

# part 2

res = 0
total = 0

part_2_lines = [list(reversed(row)) for row in zip(*lines)]
is_add = True
for line in part_2_lines:
    if "".join(line).strip() != "":
        if line[0] == '*' or line[0] == '+':
            is_add = line[0] == '+'
            res += total
            total = int("".join(line[1:]).strip()[::-1])
        else:
            num = int("".join(line).strip()[::-1])
            if is_add:
                total += num
            else:
                total *= num

res += total

print(res)
