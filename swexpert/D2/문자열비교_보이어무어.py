# T = int(input())
#
# for t in range(1, T+1):
#     pattern = input()
#     text = input()
#     s = pattern[::-1]
#     skip = list(range(len(text)))
#     i = len(pattern) - 1
#     result = 0
#
#     while i < len(text):
#         nxt = len(s)
#         j = 0
#         if s[j] == text[i]:
#             while j < len(s):
#                 if s[j] != text[i-j]:
#                     break
#                 j += 1
#             if j == len(s):
#                 result = 1
#         else:
#             while j < len(s):
#                 if s[j] == text[i]:
#                     nxt = min(j, nxt)
#                     break
#                 j += 1
#         if result:
#             break
#         i += nxt
#
#     print(result)
T = int(input())

for t in range(1, T + 1):
    pattern = input()
    text = input()
    s = pattern[::-1]
    i = len(pattern) - 1
    result = 0

    while i < len(text):
        j = 0
        nxt = len(s)
        if s[j] == text[i]:
            while j < len(pattern):
                if s[j] != text[i-j]:
                    break
                j += 1
            if j == len(s):
                result = 1
        else:
            while j < len(s):
                if s[j] == text[i]:
                    nxt = min(j, nxt)
                    break
                j += 1
        if result:
            break
        i += nxt

    print(result)
