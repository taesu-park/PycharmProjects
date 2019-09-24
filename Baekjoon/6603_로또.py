arr = []
while True:
    d = input()
    if d == '0':
        break
    arr = list(map(int,d.split()))[1:]
    arr.sort()
    result = []
    def back(n, k):
        if k == 6:
            print(*result)
            return
        for i in range(n, len(arr)):
            result.append(arr[i])
            back(i+1, k+1)
            result.pop()
    back(0, 0)
    print('')