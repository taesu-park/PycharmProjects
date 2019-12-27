N = int(input())
arr = [list(map(int,input().split()))]
union = [[] for _ in range(N)]
ans = 0
for i in range(N):
    union[i] += (list(map(int,input().split())))

def check(n):
    A, B = 0, 0



def back(k,s,A,B):
    if k == N:
        if len(A) == N or len(B) == N:
            return
        for x in range(len(A)):
            if A[x]:
                flag = check(A[x])
                if not flag:
                    return
                else:
                    ans = flag
        print(A,B)
        return
    else:
        for i in range(s,N):
            back(k+1,i+1,A+[i],B)
            back(k+1,i+1,A,B+[i])

back(0,0,[],[])
