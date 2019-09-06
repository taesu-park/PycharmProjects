from collections import deque

T = int(input())

def solution(n, m):
    if n <= m:
        
for tc in range(1, T+1):
    N = int(input())

    arr = list(input().split())
    l = []
    Q = deque()

    for i in arr:
        Q.append(list(i))
        y = Q[0][0]
        x = Q[0][0].popleft()
        if int(y) <= int(x):
            y = x

        else:
            break
        else:
            l.append(Q[0])
        Q.pop()
    l.sort()

    a = int(l.pop())
    b = int(l.pop())
    print('#{} {}'.format(tc,(a*b)))