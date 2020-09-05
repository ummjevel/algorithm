import sys

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    d = [[0]*3 for i in range(1, n+1)]

    d[1][0], d[1][1], d[1][2] = 1, 0, 0
    d[2][0], d[2][1], d[2][2] = 0, 1, 0
    d[3][0], d[3][1], d[3][2] = 1, 1, 1

    for i in range(4, n+1):
        d[i][0] = d[i-1][1] + d[i-1][2]
        d[i][1] = d[i-2][0] + d[i-2][2]
        d[i][2] = d[i-3][0] + d[i-3][1]

    ans = 0
    for i in range(3):
        ans += d[n][i]

    print(ans % 1000000009)
