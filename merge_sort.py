arr = [41, 19, 3, 7, 1014, 959, 28, 1004]
tmp = [0]*len(arr)

# def merge_sort(lo, hi):
#     if lo>=hi:
#         return
#     mid = (lo+hi)>>1
#     merge_sort(lo, mid)
#     merge_sort(mid+1, hi)
#     i, j, k = lo, mid+1, lo
#     while i<=mid and j <=hi:
#         if arr[i] <arr[j]:
#             tmp[k] = arr[i]
#             k, i = k+1,i+1
#         else:
#             tmp[k] = arr[j]
#             k,j = k+1, j+1
#     while i<=mid:
#         tmp[k] = arr[i]
#         k, i = k + 1, i + 1
#     while j <=hi:
#         tmp[k] = arr[j]
#         k, j = k + 1, j + 1
#
#     for i in range(lo, hi+1):
#         arr[i] =tmp[i]
def quick_sort(lo,hi):
    if lo>=hi:
        return
    i,j =lo,hi
    while i < j:
        while i<=hi and arr[i] <= arr[lo]:
            i+=1
        while arr[j] > arr[lo]:
            j-=1
        if i>=j: break
        arr[i],arr[j] = arr[j],arr[i]
    arr[j], arr[lo] = arr[lo],arr[j]

    quick_sort(lo, j-1)
    quick_sort(j+1,hi)


# merge_sort(0, len(arr)-1)
quick_sort(0,len(arr)-1)
print(arr)
