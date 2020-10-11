import sys

def dfs(depth, N, M):
    global visited_arr
    if depth == M:
        print(*visited_arr)
    else:
        for i in range(1, N+1):
            if len(visited_arr) == 0 or (len(visited_arr) > 0 and max(visited_arr) <= i):
                visited_arr.append(i)
                dfs(depth + 1, N, M)
                visited_arr.pop()


N, M = map(int, sys.stdin.readline().split())

visited_arr = []
dfs(0, N, M)
