import sys

def dfs(depth, N, M):
    global visited_arr
    global arr
    if depth == M:
        print(*visited_arr)
    else:
        for i in arr:
            if i not in visited_arr and (len(visited_arr) == 0 or (len(visited_arr) > 0 and visited_arr[-1] < i)):
                visited_arr.append(i)
                dfs(depth + 1, N, M)
                visited_arr.pop()


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited_arr = []
dfs(0, N, M)

# 15650 과 조건 동일. 숫자 받는 것만 다름!