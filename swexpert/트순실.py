H = [0] * 100
top = 0

def push(item):
    global top
    top += 1
    H[top] = item

    c = top
    p = c >> 1

    while p > 0 and H[c] < H[p]:
        H[c], H[p] = H[p], H[c]
        c = p
        p = c >> 1

def pop():
    global top
    ret = H[1]
    H[1] = H[top]
    top -= 1
    p, c = 1, 2

    while c <= top:
        if c + 1 <= top and H[c] > H[c + 1]:
            c += 1
        if H[c] < H[p]:
            H[c], H[p] = H[p], H[c]
            p = c
            c = p << 1
        else:
            break
    return ret


data = [69, 10, 30, 2, 16, 8, 31, 22]


for val in data:
    push(val)

while top:
    print(pop(), end=" ")
