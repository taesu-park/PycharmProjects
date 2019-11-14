N = int(input())
nums = [0]* N
def isOk(k):
    l = k + 1
    cnt = l // 2
    for i in range(2, cnt + 1):
        a, b = l-(i*2), l-i
        j = 0
        while j < i:
            if nums[a + j] != nums[b + j]:
                break
            j += 1
        if j == i:
            return False
    return True
def back(k):
    if k == N:
        print(''.join(map(str, nums)))
        return True
    for i in range(1, 4):
        nums[k] = i
        if (nums[k-1] == nums[k]) or not isOk(k):
            continue
        if back(k+1):
            return True
    return False

for i in range(1, 4):
    nums[0] = i
    if back(1):
        break
