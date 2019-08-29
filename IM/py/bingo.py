import sys
import pprint
sys.stdin = open('bingo.txt','r')

arr = [list(map(int,input().split())) for _ in range(5)]

z = 0
for _ in range(5):
    N = list(map(int,input().split()))

    for p in range(len(N)):

        for i in range(5):
            for j in range(5):
                if N[p] == arr[i][j]:
                    arr[i][j] = 0
        count = 0
        A = a = 0
        for i in range(5):
            S = s = 0
            for j in range(5):
                S += arr[i][j]
                s += arr[j][i]
                if i == j:
                    A += arr[i][i]
                if i + j == 4:
                    a += arr[i][j]
            if S == 0:
                count += 1
            if s == 0:
                count += 1

        if A == 0:
            count += 1
        if a == 0:
            count += 1
        pprint.pprint(arr)
        print(count,S,s,A,a)
        if count >=3:
            tmp=p
            break
    if count >= 3:
        print(N[p])
        break
    z += 5
print(z+p+1)

    # if A == 0:
    #     count += 1
    # if a == 0:
    #     count += 1
    # print(k, count, S, s, A, a)
    # pprint.pprint(arr)
    # if count >= 3:
        # print(k)
