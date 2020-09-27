import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
d = [[0]*2 for _ in range(n+10)]

d[1][1] = a[1]
d[1][0] = 0

for i in range(1, n):
    d[i][1] = a[i]
    d[i][0] = max(d[i-1])

    d[i] = max(d[i], d[i-1] + a[i])

print(max(d))
