import sys

mod = 1000000000

n, k = map(int, sys.stdin.readline().rstrip().split())

d = [[0]*(k+1) for _ in range(n+2)]
d[1] = [1]*(k+1)

for i in range(2, k+1):  # k자리에 관한 것.
    for j in range(n+1):  # n번째 수에 관한 것
        for k in range(j+1):  # k자리는 k-1번째 수의
            d[i][j] += d[i-1][j-k]
            d[i][j] %= mod
print(d)
