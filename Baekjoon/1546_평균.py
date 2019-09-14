N = int(input())
arr = list(map(int,input().split()))
avg = 0
maxnum = max(arr)
narr = []
for num in arr:
    num = (num/maxnum)*100
    narr.append(num)
avg = sum(narr)/N


print('{:.2f}'.format(avg))