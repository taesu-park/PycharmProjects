N = int(input())
visit = [False]*N
MAX = 0
def back(x, y, k):
    global visit, MAX
    if k < MAX:
        return
    else:
        MAX = k
    if x + y ==
    else:
        for i in range(x, N):
            if not visit[i]:
                visit[i] = True
                back(i+1, y+1, k+1)
                visit[i] = False