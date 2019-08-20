def solution(s, n):
    answer = ''
    for char in s:
        if ord(char) == 32:
            answer += chr(ord(char))
        elif not (65 <= ord(char) + n <= 90 or 97 <= ord(char) + n <= 122):
            answer += chr(ord(char) + n - 26)
        else:
            answer += chr(ord(char) + n)
    return answer


print(solution(' b', 4))