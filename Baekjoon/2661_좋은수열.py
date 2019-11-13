# def back(x, l):
#     global result
#     if len(l) >= 2:
#         for i in range(1, len(l)//2):
#             for j in range(len(l)):
#
#     if len(l) == N:
#         if int(l) < result:
#             result = int(l)
#         return
#     for i in range(x, 4):
#         back(i, l+str(i))
# N = int(input())
# result = 0
# back(1, '')

N = 3
nums = [0] * N # 수열을 저
def backtrack(k):
    if k == N:
        print(*nums)
    else:
    # k번째 위치에 1, 2, 3 중에 하나를 선택해서 수열을 생성
        for i in range(1, 4):
            nums[k] = i
            # nums[0 ~ k]
            backtrack(k + 1)
backtrack(0)