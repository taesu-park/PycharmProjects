N = int(input())
visit = [False]*N
xvisit = [False]*(N+N-1)
yvisit = [False]*(N+N-1)
MAX = 0
def back(x):
    global visit, MAX
    if x == N:
        MAX += 1
        return
    else:
        for i in range(0, N):
            if not visit[i] and not xvisit[i+x] and not yvisit[i-x+N-1]:
                xvisit[i+x] = True; yvisit[i-x+N-1] = True; visit[i] = True
                back(x+1)
                xvisit[i + x] = False; yvisit[i - x + N-1] = False; visit[i] = False

back(0)
print(MAX)