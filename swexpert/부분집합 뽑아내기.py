arr= 'ABC'; N = len(arr)
bits = [0] * N

def subset(k, n): # k = 현재 노드의 높이, n = 단말 노드의 높이
    if k == n:    # 모든 선택이 완료, 단말노드에 도착,
        for i in range(N):
            if bits[i]: print(arr[i], end = ' ')
            print()
            return
        # 선택을 계속.
    bits[k] = 1; subset(k + 1, n)   #왼쪽
    bits[k] = 0; subset(k + 1, n)   #오른쪽
subset(0, N)    # 0 = 어떤 선택도 하지 않았다.
                # N = 해야할 선택의 수



###
arr = 'ABC'; N = len(arr)
order = [0] * N         # 원소의 인덱스의 순서를 저장

def perm(k, n, used):
    if k == n:          # 하나의 순열을 생성
        for i in range(n):
            print(arr[order[i]], end=' ')
        return
    for i in range(n):
        if used & (1 << i): continue
        order[k] = i
        perm(k + 1, n, used |(1 << i))

perm(0, N, 0)           # 선택한 수 , N: 전체원소수, 0: 선택한 요소들의 집합
