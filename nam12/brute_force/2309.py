# 항상 정확도 100%를 보장하는 방법
# 장점 :거의 완벽하게 병렬 작업이 가능케 한다.
# 단점 : Complextiy에 매우 민감하다.


# combination을 쓸려고 했지만 index를 못구해서 그냥 for문 2번함.
# import sys


# dwf = []
# for i in range(9):
#     dwf.append(int(input()))

# dwf = sorted(dwf)
# dwf_s = sum(dwf)

# for i in range(9):
#     for j in range(i+1, 9):
#         if dwf_s - (dwf[i] + dwf[j]) == 100:
#             for char in dwf:
#                 if char == dwf[i] or char == dwf[j]:
#                     continue
#                 else:
#                     print(char)
