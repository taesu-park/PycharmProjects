# N, M = map(int,input().split())
# visit = [False]*(N+1)
# result = []
# def back(n):
#     if len(result) == M:
#         print(*result)
#         return
#     for i in range(n, N+1):
#         result.append(i)
#         visit[i] = True
#         back(i+1)
#         result.pop()
#         visit[i] = False
#
# back(1)

B = {x for x in range(4)} - {1, 2}
print(B)