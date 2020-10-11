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

# https://jaimemin.tistory.com/1237
# 백트래킹: https://medium.com/@jeongdowon/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-backtracking-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-13492b18bfa1

# 모르겠습니다.

# for i in range(1, N + 1):
#     for _ in range(M):
#         print(i, end=' ')
#     print()