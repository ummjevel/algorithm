import sys

# M 이 depth..
# DFS 로 구현..

def dfs(depth, N, M):
    global visited_arr
    if depth == M:
        print(*visited_arr)
    else:
        for i in range(1, N+1):
            if i not in visited_arr:
                visited_arr.append(i)
                dfs(depth + 1, N, M)
                visited_arr.remove(i)


N, M = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, N+1)]
visited_arr = []
dfs(0, N, M)


# 모르겠습니다.

# for i in range(1, N + 1):
#     for _ in range(M):
#         print(i, end=' ')
#     print()