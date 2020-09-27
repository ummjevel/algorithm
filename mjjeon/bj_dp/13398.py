n = int(input())
N = list(map(int, input().split()))

D = [0] * n
minval = 0
if min(N) < 0:
    minval = min(N)
for i in range(n):
    if minval == N[i]:
        D[i] = D[i-1]
        continue
    D[i] = max(N[i], D[i-1] + N[i]) #, D[i-1])
    
print(max(D))


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