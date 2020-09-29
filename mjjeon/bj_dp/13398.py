n = int(input())
N = list(map(int, input().split()))

D = [[0, 0] for i in range(n)]
D[0] = [N[0], -999999999]

for i in range(1, n):
    D[i][0] = max(D[i - 1][0] + N[i], N[i])
    D[i][1] = max(D[i - 1][0], D[i - 1][1] + N[i])

ans = -999999999
for i in range(n):
    ans = max(ans, max(D[i]))
print(ans)


# 틀렸습니다. 왜?
# n = int(input())
# N = list(map(int, input().split()))

# D = [[0, 0] for i in range(n)]
# D[0] = [N[0], -1000000]
# for i in range(1, n):
#     D[i][0] = max(N[i], D[i-1][0] + N[i])          # 삭제 x
#     D[i][1] = max(D[i-1][0], D[i-1][1] + N[i])     # 삭제 o
    
# print(max(max(D)))


# 틀렸습니다.

# n = int(input())
# N = list(map(int, input().split()))

# D = [0] * n
# minval = 0
# if min(N) < 0:
#     minval = min(N)
# for i in range(n):
#     if minval == N[i]:
#         D[i] = D[i-1]
#         continue
#     D[i] = max(N[i], D[i-1] + N[i]) #, D[i-1])
    
# print(max(D))