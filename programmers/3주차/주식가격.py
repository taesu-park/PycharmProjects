def solution(prices):
    answer = []
    S = [1]*(len(prices)-1)+ [0]
    print(S, len(prices)-1)
    for i in range(len(prices)-1,0,-1):

        if prices[i] >= prices[i-1]:
            S[i-1] += S[i]

    return S

print(solution([1, 2, 3, 2, 3]))

