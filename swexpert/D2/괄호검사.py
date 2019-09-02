T = int(input())

for tc in range(1, T+1):
    S = []
    a = input()
    ans = 1
    for i in a:
        if i == '(' or i == '{':
            S.append(i)
        elif i == ')' or i == '}':
            if len(S) == 0:
                ans = 0
                break
            tmp = S.pop()
            if i == ')' and tmp != '(':
                ans = 0
                break
            if i == '}' and tmp != '{':
                ans = 0
                break
    if ans and len(S) != 0:
        ans = 0
    print('#{} {}'.format(tc, ans))
