T = int(input())

for tc in range(1, T+1):
    x = input()
    ans = False
    count = 0
    tmp = 0
    for i in x:
        if i == 'O':
            tmp += 1
            count += tmp
        else:
            tmp = 0

    print(count)

