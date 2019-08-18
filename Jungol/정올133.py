n = int(input())
m = list(map(int,input().split()))

sum = 0
# for문
# for i in m:
#  sum += i
#
# avg = round(sum/n,2)
# print(avg)

# while문
i = 0
while i <= 2:
  sum+=m[i]
  i+=1
avg = round(sum/n,2)
print(avg)