N = int(input())

star = (N << 1) - 1
for i in range(N):
    print((' '*i) + ('*'*(star - i*2)) + (' ' * i))
for i in range(N):
    print((' '*i) + ('*'*(star - i*2)) + (' ' * i))
