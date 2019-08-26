arr= 'ABC'; N = len(arr)
bits = [0] * N

def subset(k, n): # k = 현재 노드의 높이, n = 단말 노드의 높이
    global N, K, ans
    if k == n:    # 모든 선택이 완료, 단말노드에 도착,
        cnt = S = 0
        for i in range(N):
            if bits[i]:
                cnt , S = cnt + 1, S + (i + 1)
        if cnt == N and S == K:
            ans += 1
        else:
            bits[k] = 1; subset(k + 1, n)   #왼쪽
            bits[k] = 0; subset(k + 1, n)   #오른쪽
    # 0 = 어떤 선택도 하지 않았다.
                # N = 해야할 선택의 수

T = int(input())
for tc in range(1, T +1):
    N, K = map(int,input().split())
    ans = 0
    subset(0, 12)
    print(tc, ans)