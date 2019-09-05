# # L, C = map(int,input().split())
# # arr = list(input().split())
# # visit = [False for _ in range(L+1)]
# # arr.sort()
# # print(arr)
# # ans = []
# # def DFS(n):
# #     S = []
# #     S.append(n)
# #     visit[n] = True
# #     for i in range(len(arr)):
# #         if not visit[i] and len(S) < 4:
# #             DFS(i)
# #     if len(S) == 4:
# #         ans += S
# #         S = []
# # DFS(arr[0])
# # print(visit)
#
#
# ## 부분집합
# pwd = []
# vowel = ('a','e','i','o','u')
# def backtrack(k, mo, ja):
#     if len(pwd) == L:
#         print(pwd)
#         return
#     if k == C: return
#     pwd.append(arr[k])
#     a = b = 0
#     if arr[k] in vowel: a = 1
#     else: b = 1
#     backtrack(k + 1, mo + a, ja + b)    # k 번째 요소를 포함하는 경우
#     pwd.pop()
#     backtrack(k + 1, mo, ja)    # k 번째 요소를 포함하지 않는 경우
#
#
# L, C = map(int,input().split())
# arr = list(input().split())
# arr.sort()
# backtrack(0)
#
# ## 조합생성(3C2)
# arr = 'ABC'; N = len(arr)
#
# for i in range(N):
#     for j in range(i+1, N): # 조합
#         if i==j: continue # 순열
#         print(arr[i], arr[j])
# #
# for i in range(N):
#     for j in range(i, N): # 중복조합
#         if i==j: continue # 순열
#         print(arr[i], arr[j])

# 5C3
arr = 'ABCDE'; N = len(arr)
N, R = 5, 3
choose = []

def comb(k, start):
    if k == R:
        print(choose)
        return
    for i in range(start, N):
        choose.append(arr[i])
        comb(k + 1, i+1 ) # i+1 -> i : 중복조합
        choose.pop()
comb(0, 0)
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             print(arr[i], arr[j], arr[k])