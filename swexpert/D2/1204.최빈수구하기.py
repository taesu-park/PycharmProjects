T = int(input())

for x in range(1, T+1):
    a = int(input())
    score = list(map(int,input().split()))
    count = [0]*101
    maxidx = 0
    for s in score:
        count[s] += 1
    for i in range(1, 101):
        if score[maxidx] <= score[i]:
            maxidx = i
    print('#{} {}'.format(x, maxidx))

