num = int(input())

def star(i, j):
    while i != 0:
        if i % 3 == 1 and j % 3 ==1:
            print(' ', end='')
            return None
        i = i//3
        j = j//3
    print('*', end='')

for i in range(num):
    for j in range(num):
        star(i, j)
    print('\n', end='')

