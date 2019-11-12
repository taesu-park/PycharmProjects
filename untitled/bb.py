def solution(user_id, banned_id):
    answer = 1
    result = {}
    for ban in banned_id:
        for user in user_id:
            if len(user) != len(ban):
                continue
            for i in range(len(ban)):
                if ban[i] == user[i] or ban[i] == '*':
                    continue
                else:
                    break
            else:
                if result.get(ban):
                    result[ban] += 1
                else:
                    result.update({ban: 1})
    for x in result.values():
        answer *= x

    return answer

user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))