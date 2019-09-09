arr = []
for _ in range(10):
    num = int(input())
    arr.append(num%42)

numlist = set(arr)
print(len(numlist))