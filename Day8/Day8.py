import sys
import re
import math
io = sys.stdin
lines = []
for line in io:
    lines.append([int(x) for x in line.strip().split(',')])

distances = {}

for i in range(len(lines)):
    for j in range(0, i):
        distances[(i,j)] = math.sqrt((lines[i][0] - lines[j][0])**2 + (lines[i][1] - lines[j][1])**2 + (lines[i][2] - lines[j][2])**2)

# pairs = 10
pairs = 1000
connections = ([x for x in dict(sorted(distances.items(), key = lambda item: item[1]))])

sets = []
for connection in connections[:pairs]:
    new_sets = []
    current_set = set()
    current_set.add(connection[0])
    current_set.add(connection[1])
    for set_ in sets:
        if current_set & set_:
            current_set = current_set.union(set_)
        else:
            new_sets.append(set_)
    new_sets.append(current_set)
    sets = new_sets
print(math.prod(sorted([len(x) for x in sets])[-3:]))

sets = []
for connection in connections:
    new_sets = []
    current_set = set()
    current_set.add(connection[0])
    current_set.add(connection[1])
    for set_ in sets:
        if current_set & set_:
            current_set = current_set.union(set_)
        else:
            new_sets.append(set_)
    new_sets.append(current_set)
    sets = new_sets
    if (len(new_sets) == 1) and len(new_sets[0]) == len(lines):
        # all connected
        print(lines[connection[0]][0] * lines[connection[1]][0])
        break
