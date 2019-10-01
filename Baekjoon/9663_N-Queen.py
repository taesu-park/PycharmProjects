N = int(input())
visit = [False]*N
xvisit = [False]*(N+N-1)
yvisit = [False]*(N+N-1)
MAX = 0
def back(x,k):
    global visit, MAX
    if x == N:
        return
    else:
        for i in range(0, N):
            if not visit[i] and not xvisit[i] and not yvisit[i]:
                xvisit[i+x] = True; yvisit[i-x+N-1] = True; visit[i] = True
                back(x+1, k+1)
                xvisit[i + x] = False; yvisit[i - x + N-1] = False; visit[i] = False
    if k > MAX:
        MAX = k
back(0,0)
print(MAX)