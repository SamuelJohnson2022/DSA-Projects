# Samuel Johnson - sdj5203
# Nikita Petrenko - nmp5361
# Jason Novillo - jxn262

class Interval:
    def __init__(self, s, t, v):
        self.s = s
        self.t = t
        self.v = v

    def __lt__(self, other):
        if self.t == other.t:
            return self.s < other.s
        else:
            return self.t < other.t


intervals = []


def binary_search(k, a, b):
    global intervals

    if b <= a:
        return -1

    m = int((a + b)/2)

    if(intervals[m + 1].t >= intervals[k-1].s and intervals[k-1].s >= intervals[m].t):
        return m

    if(intervals[m].t >= intervals[k-1].s):
        return binary_search(k, a, m)

    if(intervals[k-1].s >= intervals[m + 1].t):
        return binary_search(k, m+1, b)


def search(k):
    global intervals

    index = 0

    while(intervals[index].t <= intervals[k].s):
        index += 1

    return index


num_of_jobs = int(input())


for i in range(num_of_jobs):
    line_input = list(map(int, input().split()))
    interval = Interval(line_input[0], line_input[1], line_input[2])
    intervals.append(interval)

# Sort the intervals based on the t value
intervals.sort()

F = []
F.append(0)

for i in range(1, len(intervals) + 1):
    F.append(max(F[i - 1], intervals[i - 1].v +
                 F[search(i - 1)]))

print(F[len(intervals)])
