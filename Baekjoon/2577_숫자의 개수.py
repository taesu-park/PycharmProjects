a = int(input())
b = int(input())
c = int(input())

num = a*b*c
arr = list(str(num))
s = [0]*10
for i in arr:
    s[int(i)] += 1

for x in s:
    print(x)

