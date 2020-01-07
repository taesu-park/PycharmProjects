T = int(input())

for tc in range(1, T+1):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    for i in range(len(plan)):
        if i:
