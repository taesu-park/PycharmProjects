N = int(input())

def factorial(n):
    ans = 1
    while n >= 1:
        ans *= n
        n -= 1
        factorial(n)
    return ans
print(factorial(N))