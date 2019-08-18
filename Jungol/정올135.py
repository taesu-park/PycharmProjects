a, b = map(int,input().split())
if a>b:
    a, b = b, a
sum = 0
avg = 0
count = 0

while a <= b:
    if not a % 3 or not a % 5:
        sum += a
        count += 1
    a += 1

avg = sum / count

print('sum : {}'.format(sum))
print('avg : {:.1f}'.format(avg))

# for문
# sum = 0
# avg = 0
# count = 0
# for i in range(a, b+1):
#  if not i % 3 or not i % 5:
#  sum += i
#  count += 1
# avg = sum/count
#
# print('sum : {}'.format(sum))
# print('avg : {:.1f}'.format(avg))
