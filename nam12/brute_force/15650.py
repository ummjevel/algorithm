from itertools import permutations

n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

check = False
for c in permutations(arr, m):
    check = False
    for i in range(len(c)-1):
        if int(c[i]) < int(c[i+1]):
            check = True
        else:
            check = False
            break
    if(check):
        print(" ".join(map(str, c)))
