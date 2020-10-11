import sys

def dfs(depth, N, M, cur_i_idx):
    global visited_arr
    global arr
    is_found = False    # 중복된 수열일 경우(True) 출력하지 않고 넘어가도록..
    is_in = False       # 중복된 숫자가 포함된 경우(True) 출력 후 리스트에 추가한다.(is_found 가 False일 경우에만, True 면 중복이 되버림..)
    if depth == M:
        for i in dup_list:
            if i in visited_arr:
                is_in = True
                for visited_list in dup_visited:
                    if visited_list == visited_arr:
                        is_found = True
                        break
            if is_found == True:
                break
        if is_found == False:
            print(*visited_arr)
        if is_in == True and is_found == False:
            dup_visited.append(visited_arr)
    else:
        for i in range(len(arr)):
            # 현재 arr의 index를 넘겨받아서 그것만 같은지 확인하기..
            if i != cur_i_idx:
                visited_arr.append(arr[i])
                dfs(depth + 1, N, M, i)
                visited_arr.pop()


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

count = {}
for i in arr:
    try:
        count[i] += 1
    except:
        count[i] = 1
dup_list = [i for idx, value in count.items() if value == 2]
dup_visited = []
visited_arr = []
dfs(0, N, M, -1)

# 15652 과 조건 동일. 숫자 받는 것만 다름!