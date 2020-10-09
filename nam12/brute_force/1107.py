# +, -, 채널입력
# 채널 0에서 -누르면 그대로임.

# 목표 채널을 구하기 위해서
# 1. 주어진 배열의 수들을 len만큼 조합해서 모두 만들어보고
# 그 차이의 절댓값이 가장 작은 것을 고른다.
# 그리고 +, - 로 접근하기
# 2. +,- 로만 접근한 것이 채널이동 보다 작은지 확인해주기.

from itertools import permutations

cur = 100  # 시작 채널.
cnt = [0, 0]

goal = input()
leng = len(goal)

n = int(input())
remove_list = list(map(int, input().split()))
remocon_list = [i for i in range(10)]

for i in range(n):
    remocon_list.remove(remove_list[i])

print(remocon_list)

# while True:  # 번호이동후 +,- 로 체크하기.
#     if cur == goal:
#         break

min_value = 600000
for c in permutations(remocon_list, leng):  # 순열함수 쓰면 tuple로 나오는데 변환시키는게 지랄같음.
    if c[0] == (int(goal[0])-1) or c[0] == int(goal[0]) or c[0] == (int(goal[0])+1):
        temp = "".join(map(str, c))
        min_value = min(min_value, abs(int(goal) - int(temp)))
cur = min_value
print(cur)

if cnt[0] > abs(goal - cur):
    print(cnt[0])
    exit()
else:
    print(abs(goal - cur))
