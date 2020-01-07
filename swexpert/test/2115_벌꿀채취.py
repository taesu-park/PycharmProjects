T = int(input())

for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    