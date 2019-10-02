def hor(arr):
    global maxV
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        if temp > maxV:
            maxV = temp
def ver(arr):
    global maxV
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        if temp > maxV:
            maxV = temp

def cross(arr):
    global maxV
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    if temp > maxV:
        maxV = temp

    temp2 = 0
    for i in range(100):
        temp2 += arr[i][99-i]
    if temp2 > maxV:
        maxV = temp2

for tc in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = 0
    hor(arr)
    ver(arr)
    cross(arr)
    print('#{} {}'.format(t, maxV))