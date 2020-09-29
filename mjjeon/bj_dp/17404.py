import sys
N = int(sys.stdin.readline())
D = [[0,0,0] for i in range(N)]
result = 100000
input_list = []
# for i in range(1, N):
# # for i in range(N - 1):
#     house = list(map(int, sys.stdin.readline().split()))
#     D[i][0] = min(D[i-1][1], D[i-1][2]) + house[0]
#     D[i][1] = min(D[i-1][0], D[i-1][2]) + house[1]
#     D[i][2] = min(D[i-1][0], D[i-1][1]) + house[2]

# house = list(map(int, sys.stdin.readline().split()))
# D[N-1][0] = min(D[N-2][1], D[N-2][2], D[0][1], D[0][2]) + house[0]
# D[N-1][1] = min(D[N-2][0], D[N-2][2], D[0][0], D[0][2]) + house[1]
# D[N-1][2] = min(D[N-2][0], D[N-2][1], D[0][0], D[0][1]) + house[2]

# house = list(map(int, sys.stdin.readline().split()))
# D[0][0] = min(D[-1][1], D[-1][2]) + house[0]
# D[0][1] = min(D[-1][0], D[-1][2]) + house[1]
# D[0][2] = min(D[-1][0], D[-1][1]) + house[2]


for i in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))

for index in range(3):
    D[0] = [1000000, 1000000, 1000000]
    D[0][index] = input_list[0][index]
    
    for i in range(1, N):
        D[i][0] = min(D[i-1][1], D[i-1][2]) + input_list[i][0]
        D[i][1] = min(D[i-1][0], D[i-1][2]) + input_list[i][1]
        D[i][2] = min(D[i-1][0], D[i-1][1]) + input_list[i][2]

    if index == 0:
        D[N-1][0] = 100000
        D[N-1][1] = min(D[N-1][0], D[N-1][2]) + input_list[N-1][1]
        D[N-1][2] = min(D[N-1][0], D[N-1][1]) + input_list[N-1][2]
    elif index == 1:
        D[N-1][0] = min(D[N-1][1], D[N-1][2]) + input_list[N-1][0]
        D[N-1][1] = 100000
        D[N-1][2] = min(D[N-1][0], D[N-1][1]) + input_list[N-1][2]
    elif index == 2:
        D[N-1][0] = min(D[N-1][1], D[N-1][2]) + input_list[N-1][0]
        D[N-1][1] = min(D[N-1][0], D[N-1][2]) + input_list[N-1][1]
        D[N-1][2] = 100000

    result = min(result, min(D[N-1]))
    print(D)


print(result)