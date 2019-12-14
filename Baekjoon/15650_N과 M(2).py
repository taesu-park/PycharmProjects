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

N, M = map(int,input().split())
def back(x, y, k):
    if y == M:
        print(*x)
        return
    else:
        for i in range(k+1, N+1):
            back(x+[i], y+1, i)
back([],0, 0)