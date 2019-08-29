N = int(input())
arr = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
tmp = []
## 재귀
# def BinarySearch(a, low, high, key):
#     if low > high:
#         return '0'
#     else:
#         middle = (low + high) // 2
#         if key == a[middle]:
#             return '1'
#         elif key < a[middle]:
#             return BinarySearch(a, low, middle-1, key)
#         elif a[middle] < key:
#             return BinarySearch(a, middle +1, high, key)

def binarySearch(a, key):
    start = 0
    m = len(a) - 1
    while start <= m:
        middle = (start + m) // 2
        if a[middle] == key:

            return '1'
        elif a[middle] > key:
            m = middle -1
        else:
            start = middle +1

    return '0'

# arr를 정렬시키고
# for i in range(len(arr)-1, 0, -1):
#     for j in range(0, i):
#         if arr[j] >= arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
arr.sort()

# arr2에서 값을 하나하나빼와서 arr에 대조
for j in arr2:

    tmp.append(binarySearch(arr,j))
# 값을 찾으면 arr2의 인덱스값을 리턴
print(' '.join(tmp))


