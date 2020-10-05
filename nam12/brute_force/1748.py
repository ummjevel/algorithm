n = input()
leng = len(n)

cnt = 1
n = int(n)

# if leng == 1:
#     print(n * 1)
#     exit()
# elif leng == 2:
#     print((n-9)*2 + 9 * 1)
#     exit()
# elif leng == 3:
#     print((n-99)*3 + 90*2 + 9)
#     exit()
# elif leng == 4:
#     print(n - 999 + 900 + 90 + 9)
# elif leng == 5:

# elif leng == 6:

# elif leng == 7:

# elif leng == 8:

# elif leng == 9:
minus = 0
for i in range(leng-2, -1, -1):
    minus += 9 * (10**i)

for i in range(leng-2, -1, -1):
    cnt += i*9*(10**i)
    print(i)
    print(i*9*(10**i))

print(leng*(n-minus) + cnt)
