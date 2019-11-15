def cook(A, B):
    global ans
    result = 0
    result2 = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            result += (S[A[i]][A[j]] + S[A[j]][A[i]])
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            result2 += (S[B[i]][B[j]] + S[B[j]][B[i]])
    if abs(result - result2) < ans:
        ans = abs(result - result2)
def back(k):
    if len(A) == N//2:
        B = list({x for x in range(N)} - set(A))
        # print(A, B)
        cook(A, B)
        return
    else:
        # A.append(k)
        # back(k+1)
        # A.pop()
        # B.append(k)
        # back(k+1)
        # B.pop()
        for i in range(k, N):
            if i not in A:
                A.append(i)
                back(i+1)
                A.pop()

T = int(input())
for tc in range(1, T+1):
    global result
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    A, B = [],[]
    ans = 0xfffffff
    back(0)
    print('#{} {}'.format(tc,ans))

