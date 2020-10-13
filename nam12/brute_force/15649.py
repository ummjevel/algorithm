# from itertools import permutations

# n, m = map(int, input().split())
# arr = []
# for i in range(1, n+1):
#     arr.append(i)

# for c in permutations(arr, m):
#     print(" ".join(map(str, c)))

n, m = map(int, input().split())
check = [False] * n
num = [i for i in range(1, n+1)]
arr = []


def dfs(idx):
    if(idx == m):
        print(*arr)
        return

    for i in range(n):
        if(check[i]):
            continue

        check[i] = True
        arr.append(num[i])
        dfs(idx+1)
        arr.pop()
        print(arr)
        check[i] = False


dfs(0)
