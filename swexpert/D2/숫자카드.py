T = int(input())

for i in range(1, T+1):
    a = input()
    b = list(input())
    count = [0]*10
    for num in b:
        count[int(num)] += 1
    idxnum = 0
    countmax = count[0]
    for idx,j in enumerate(count):
        if j >= countmax:
            countmax = j
            idxnum = idx
    print(idxnum, countmax)