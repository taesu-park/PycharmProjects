# N, M = map(int,input().split())
# result = []
# visit = [0]*(N+1)
# def back(n):
#     if len(result) == M:
#         print(*result)
#         return
#     for i in range(1, N+1):
#         if not visit[i]:
#             result.append(i)
#             visit[i] = 1
#             back(i)
#             visit[i] = 0
#             result.pop()
# back(1)
#

N, M = map(int,input().split())
def back(x, y):
    if y == M:
        print(*x)
        return
    else:
        for i in range(1, N+1):
            if i in x:
                continue
            else:
                back(x+[i], y+1)
back([],0)
