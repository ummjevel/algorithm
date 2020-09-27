import sys

n = int(sys.stdin.readline().rstrip())

p = [[0]*3 for _ in range(n+1)]
d = [[0]*3 for _ in range(n+1)]
path = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    p[i] = list(map(int, (sys.stdin.readline().rstrip().split())))

# d[1][0].append(p[1][0])
# d[1][1].append(p[1][1])
# d[1][2].append(p[1][2])

print(p, d)
print(p[1][0])
d[1][0]
