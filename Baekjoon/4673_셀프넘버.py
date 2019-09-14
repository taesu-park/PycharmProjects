result = [x for x in range(1, 10001)]
ans = []

def d(n):
    x = 0
    for i in str(n):
        x += int(i)
    return n + x

for j in range(1, 10001):
    k = d(j)
    ans.append(k)
number = sorted(list(set(result) - set(ans)))
for _ in number:
    print(_)
