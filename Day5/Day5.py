import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

is_ranges = True

ranges = []
ids = []
for line in lines:
    if line == "":
        is_ranges = False
    else:
        if is_ranges:
            ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
        else:
            ids.append(int(line))

num_fresh = 0

for id_ in ids:
    fresh = False
    for range_ in ranges:
        if id_ >= range_[0] and id_ <= range_[1]:
            fresh = True
            break
    if fresh:
        num_fresh += 1

print(num_fresh)

fresh_ranges = [[range_[0], range_[1]] for range_ in ranges]

stop = False

while (not stop):
    stop = True
    temp = []
    for range_ in fresh_ranges:
        can_append = False
        for fresh_range in temp:
            ## 4 cases: overlaps the bottom, overlaps the top, completely inside, or completely outside

            # overlaps the bottom
            if range_[0] < fresh_range[0] and range_[1] >= fresh_range[0] and range_[1] <= fresh_range[1]:
                can_append = True
                fresh_range[0] = range_[0]

            # overlaps the top
            if range_[1] > fresh_range[1] and range_[0] >= fresh_range[0] and range_[0] <= fresh_range[1]:
                can_append = True
                fresh_range[1] = range_[1]

            # completely inside
            if range_[0] >= fresh_range[0] and range_[0] <= fresh_range[1] and range_[1] >= fresh_range[0] and range_[1] <= fresh_range[1]:
                can_append = True

            # completely outside
            if range_[1] > fresh_range[1] and range_[0] < fresh_range[0]:
                can_append = True
                fresh_range[0] = range_[0]
                fresh_range[1] = range_[1]

        if can_append:
            stop = False
        else:
            temp.append([range_[0], range_[1]])

    fresh_ranges = temp

total = 0

for fresh_range in fresh_ranges:
    total += fresh_range[1] - fresh_range[0] + 1


print(total)