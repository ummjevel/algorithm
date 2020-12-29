N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num = list(set(num_list))
num.sort()
n = len(num)

check = [False for i in range(N)]
ans = []


def dfs(cnt):

    if cnt == M:
        print(*ans)
        return

    for i in range(n):

        if (check[i]):
            continue

        check[i] = True
        ans.append(num[i])
        dfs(cnt+1)
        ans.pop()
        check[i] = False


def dfs2(cnt):

    if cnt == M:
        print(*ans)
        return

    for i in range(n):

        if (check[i]):
            continue

        ans.append(num[i])
        dfs2(cnt+1)
        check[i] = True
        ans.pop()
        check[i] = False


if n > M:
    dfs(0)
else:
    dfs2(0)
