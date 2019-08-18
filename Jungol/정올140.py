num = list(map(int,input().split()))

sum = 0
avg = 0
count = 0
for i in num:
    sum +=i
    count += 1
if num[len(num)-1]==0:
    count -=1

avg = sum / count
print('{} {:.0f}'.format(sum, avg))