T = int(input())

def code(n, m, l):
    global result, num
    tmp = []
    ans = ''
    l += 7
    if l == 63:
        return
    for y in range(7):
        tmp.append(arr[n][m-y])
    ans = ''.join(tmp)
    result.append(num[ans[::-1]])
    code(i, m-7, l)

for tc in range(1, T+1):
    num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    result = []
    aaa = 0
    k = 0
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                code(i, j, k)
                break
        if result:
            break
    num = 0
    aaa = (result[7] + result[5] + result[3] + result[1])*3 + result[6] + result[4] + result[2]+result[0]

    if not aaa % 10:
        print('#{} {}'.format(tc,sum(result)))

    elif aaa % 10:
        print('#{} {}'.format(tc, 0))