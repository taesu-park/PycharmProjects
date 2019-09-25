L, C = map(int,input().split())
arr = list(input().split())
visit = [False]*C
vowel = {'a','e','i','o','u'}
arr.sort()

def back(x, y, z, result):
    global vowel
    if len(result) == L:
        if y >= 1 and z >= 2:
            print(result)
        return
    else:
        for i in range(x, C):
            if arr[i] in vowel:
                back(i+1, y+1, z, result+arr[i])
            else:
                back(i+1, y, z + 1, result+arr[i])



back(0, 0, 0, '')