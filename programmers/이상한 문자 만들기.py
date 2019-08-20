def solution(s):
    answer = ''

    for idx, char in enumerate(s):
        tmp = ''
        if not idx & 1:
            tmp += char.upper()
        else:
            tmp += char.lower()

    return answer

print(solution('aAaA   bBBBbaaa'))