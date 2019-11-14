def cook():
    pass
def back(k):
    if k == N:
        if len(A) == N//2 == len(B):
            print(A, B)
        return
    else:
        A.append(k)
        back(k+1)
        A.pop()
        B.append(k)
        back(k+1)
        B.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    A, B = [],[]
    for a in range(N):
        back(a)
    # for i in range(N):
    #     for j in range(N):
    #         if S[i][j] != 0