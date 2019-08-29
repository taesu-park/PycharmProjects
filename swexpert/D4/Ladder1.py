import sys
sys.stdin = open('input_Ladder.txt','r')


for t in range(1, 11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    # for x in range(100):
    #     for y in range(100):
print(arr)