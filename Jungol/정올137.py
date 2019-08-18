row,col = map(int,input().split())

# for문
for x in range(1,row+1):
    for y in range(1,col+1):
        print(x*y, end=' ')
    print()

