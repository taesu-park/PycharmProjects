T = int(input())
result = []
for tc in range(1, T+1):
    N , arr = input().split()
    x = format(int(arr, 16), 'b')
    print('#{} {}'.format(tc,'0'*(int(N)*4-len(x))+ x))
