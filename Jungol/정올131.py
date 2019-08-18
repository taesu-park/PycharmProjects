a, b = map(int,input().split())

if a>b:
    a,b = b,a

for i in range(a, b+1):
    print(i, end=' ')

while a<=10:
    print(a)
    a += 1
    