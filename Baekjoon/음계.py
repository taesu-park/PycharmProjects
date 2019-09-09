arr = list(map(int,input().split()))
s = arr[0]
result = 'mixed'

if arr == sorted(arr):
    result = 'ascending'
elif arr == sorted(arr, reverse=True):
    result = 'descending'

print(result)