def solution(numbers, target):
    answer = 0
    result = 0
    for i in range(len(numbers)):
        check(numbers[i], 0, target)
    return answer

def check(x, result, target):
    global answer
    if result == target:
        answer += 1
        return
    else:
        if result < target:
            result += x
        else:
            result -= x
