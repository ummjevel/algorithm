# from itertools import permutations

# n, m = map(int, input().split())
# arr = []
# for i in range(1, n+1):
#     arr.append(i)

# check = False
# for c in permutations(arr, m):
#     check = False
#     for i in range(len(c)-1):
#         if int(c[i]) < int(c[i+1]):
#             check = True
#         else:
#             check = False
#             break
#     if(check):
#         print(" ".join(map(str, c)))

# 순열이랑 조합쓰면 좋을 줄 알았는데 index 구하기도 힘들고,
# 무조건 tuple로 반환되는거라 원소마다 형변환 비교해줘서 별로인듯.
# case가 클 땐 재귀로 돌리는 brute force가 제일 나은거 같다.(back tracking)
