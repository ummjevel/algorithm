# +, -, 채널입력
# 채널 0에서 -누르면 그대로임.

# 목표 채널을 구하기 위해서 
# 1. 주어진 배열의 수들을 len만큼 조합해서 모두 만들어보고
# 그 차이의 절댓값이 가장 작은 것을 고른다.
# 그리고 +, - 로 접근하기
# 2. +,- 로만 접근한 것이 채널이동 보다 작은지 확인해주기.

cur = 100 #시작 채널.
cnt = 0

goal = int(input())

n = int(input())
remove_list = list(map(int, input().split()))
remocon_list = [for i in range(10)]

while True :
    if cur == goal :
        break
    
    for i in range (10) :


