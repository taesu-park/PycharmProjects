
N = int(input())
game = ['3', '6', '9']
result = []

for i in range(1, N + 1):
    tmp = ''
    for j in range(len(str(i))):
        if tmp and str(i)[j] in game:
            tmp += '-'
        elif str(i)[j] in game:
            tmp = '-'
    if tmp:
        result.append(tmp)
    else:
        result.append(str(i))
print(*result)