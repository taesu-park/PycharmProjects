n = int(input())

i = 1
tmp = 0
while not i == 0:
    print('*' * i)
    if i == n:
        tmp += 1
    if tmp == 1:
        i -= 1
    else:
        i += 1