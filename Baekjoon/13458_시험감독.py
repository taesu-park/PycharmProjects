N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

result = N
for i in A:
    if B < i:
        if not (i - B)%C:
            result += (i - B)//C
        else:
            result += (i - B)//C +1
    else:
        continue

print(result)