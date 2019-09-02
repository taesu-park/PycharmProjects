def solution(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3

    if memo[n] != 0:
        return memo[n]

    memo[n] = solution(n - 1, memo) + solution(n - 2, memo)*2
    return memo[n]




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N = N//10
    memo = [0]*(N+1)
    print('#{} {}'.format(tc, solution(N, memo)))