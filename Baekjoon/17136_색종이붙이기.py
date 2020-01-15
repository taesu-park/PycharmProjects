def solve(x,y):
    flag = 0
    while not flag:
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx, ty = x+dx, y+dy
            if tx < 0 or tx >= 10 or ty < 0 or ty >= 10:
                continue



board = [list(map(int,input().split())) for _ in range(10)]
confetti = [[1], [[1,1],[1,1]],[[1,1,1],[1,1,1],[1,1,1]],[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]]
for z in range(4,-1):
    for i in range(10-z-1):
        for j in range(10-z-1):
            if board[i][j] == confetti[z]: