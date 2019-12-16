# # 브루트포스
# N = int(input())
# T = [list(map(int,input().split())) for _ in range(N)]
# ans = 0
# def back(x, use):
#     global ans
#     if x == N:
#         ans = max(use,ans)
#         return
#     if x > N:
#         return
#     back(x+1, use)
#     back(x+T[x][0],use+T[x][1])
# back(0,0)
# print(ans)

# 다이나믹프로그래밍
N = int(input())
t = []
p = []
dp = []
for i in range(N):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(N-1, -1, -1):
    if t[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],p[i]+dp[i+t[i]])
print(dp[0])