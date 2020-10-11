import sys

def dfs(depth, N, M):
    global visited_arr
    global arr
    if depth == M:
        print(*visited_arr)
    else:
        for i in arr:
            if i not in visited_arr:
                visited_arr.append(i)
                dfs(depth + 1, N, M)
                visited_arr.pop()


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited_arr = []
dfs(0, N, M)

# 숫자들을 입력 받아서 입력받은 숫자에서 출력하도록 하는 거라서 입력받고, 오름차순이어야 하므로 정렬해줌.