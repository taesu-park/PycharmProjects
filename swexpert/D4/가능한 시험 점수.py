#
# def back(x,y):
#     global l
#     if x not in l:
#         l.append(x)
#
#     for i in range(y,len(arr)):
#         back(x+arr[i],i+1)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     l = []
#     back(0,0)
#     print('#{} {}'.format(tc,len(l)))

# 1.
# N = 3
# scores = [2, 3, 5]
# visit = [[0]*(N * 100 + 1) for _ in range(N + 1)]
# cnt = 0
# def backtrack(k, s):
#     if visit[k][s]:return
#     visit[k][s] = 1
#     if k == N:
#         global cnt
#         cnt += 1
#     else:
#         backtrack(k+1, s)
#         backtrack(k+1, s + scores[k])
# backtrack(0, 0)
# print(cnt)

# 2.
# import collections
# scores = [2, 3, 5]
# N = len(scores)
# visit = [[0]* (N * 100 + 1) for _ in range(N+1)]
# cnt = 0
#
# Q = []
# Q.append(0)
# for k in range(len(scores)):
#     for i in range(len(Q)):
#         t = Q[i] + scores[k]
#         if visit[k][t] == 0:
#             Q.append(t)
#             visit[k][t] = 1
# print(len(Q))
#
# def back(x,y):
#     global l
#     if x not in l:
#         l.append(x)
#
#     for i in range(y,len(arr)):
#         back(x+arr[i],i+1)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     l = []
#     back(0,0)
#     print('#{} {}'.format(tc,len(l)))

# 1.
# N = 3
# scores = [2, 3, 5]
# visit = [[0]*(N * 100 + 1) for _ in range(N + 1)]
# cnt = 0
# def backtrack(k, s):
#     if visit[k][s]:return
#     visit[k][s] = 1
#     if k == N:
#         global cnt
#         cnt += 1
#     else:
#         backtrack(k+1, s)
#         backtrack(k+1, s + scores[k])
# backtrack(0, 0)
# print(cnt)

# 2.
import collections
scores = [2, 3, 5]
N = len(scores)
visit = [[0]* (N * 100 + 1) for _ in range(N+1)]
cnt = 0

Q = []
Q.append(0)
for k in range(len(scores)):
    for i in range(len(Q)):
        t = Q[i] + scores[k]
        if visit[k][t] == 0:
            Q.append(t)
            visit[k][t] = 1
print(len(Q))
def back(x,y):
    global count
    if visit[x][y]:
        return
    visit[x][y] = 1
    if x == N:
        count += 1
        return
    else:
        back(x+1,y)
        back(x+1,y+arr[x])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    visit = [[0]*(N*100+1) for _ in range(N+1)]
    arr = list(map(int,input().split()))
    back(0,0)
    print('#{} {}'.format(tc,count))