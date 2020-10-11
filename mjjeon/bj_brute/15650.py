import sys

def dfs(depth, N, M):
    global visited_arr
    if depth == M:
        print(*visited_arr)
    else:
        for i in range(1, N+1):
            if i not in visited_arr and (len(visited_arr) == 0 or (len(visited_arr) > 0 and visited_arr[-1] < i)):
                visited_arr.append(i)
                dfs(depth + 1, N, M)
                visited_arr.remove(i)


N, M = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, N+1)]
visited_arr = []
dfs(0, N, M)

# 15649 문제에서 조건만 추가..!