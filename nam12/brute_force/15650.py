from itertools import permutations

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)
arr.append(100000)

check = False
for c in permutations(arr, m):
    for i in c:
        if int(i) < int(i+1):
            check = True
    if(check):
        print(" ".join(map(str, c)))
