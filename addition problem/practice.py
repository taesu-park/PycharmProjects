a = '123456789'
l = []
# tmp = ''
# for idx, i in enumerate(a):
#     tmp += i
#     if idx % 3 == 2:
#         l.append(list(tmp))
#         tmp = ''

# print(l)

for i in range(0,9,3):
    l.append(list(a[i:i+3]))
print(l)
# for k in range(3):
#     result = ''
#     for m in range(3):
#         result += str(l[k][m])
#
#     print(result)
# result = ''
# for j in l:
#     result = ''.join(j)
#
#     print(result)

for m in range(3):
    result = ''
    for n in range(3):
        result+= ''.join(l[n][m])
    print(result)