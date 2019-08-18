n = list(map(int,input().split()))

# for문

odd = 0
even = 0

# for i in n:
#  if i%2:
#  odd += 1
#  else:
#  even += 1
# print('even : {}'.format(even))
# print('odd : {}'.format(odd))

# while문
i = 0
while i<=len(n)-1:
  if n[i] % 2:
  odd += 1
  else:
  even += 1
  i += 1

print('even : {}'.format(even))
print('odd : {}'.format(odd))