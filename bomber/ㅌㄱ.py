# import sys
# sys.stdin = open('xr.txt','a+')
#
# for t in range(5):
#     arr = input().split()
#
# print(arr)
#
# f.close()
import sys
sys.stdin = open('xr.txt','r')


arr = []
f = open('xr.txt', 'r')
for i in range(5):
    arr += (input().split())
print(arr)

f = open("xr.txt",'a+')
arr[1] = arr[3]
f.write(arr[1])
f.close()

