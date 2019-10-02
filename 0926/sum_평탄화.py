def hor(arr, b):
    global minV, min_b
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += abs(arr[i][j]-b)
            if temp > minV:
                break
        if temp < minV:
            minV = temp
            min_b = b
def ver(arr, b):
    global minV, min_b
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += abs(arr[j][i]-b)
            if temp > minV:
                break
        if temp < minV:
            minV = temp
            min_b = b
def cross(arr, b):
    global minV, min_b
    temp = 0
    for i in range(100):
        temp += abs(arr[i][i]-b)
        if temp > minV:
            break
    if temp < minV:
        minV = temp
        min_b = b
    temp2 = 0
    for i in range(100):
        temp2 += abs(arr[i][99-i]-b)
        if temp2 > minV:
            return
    if temp2 < minV:
        minV = temp2
        min_b = b

for tc in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    minV = 29 * 100
    min_b = 29
    for b in range(1,30):
        hor(arr, b)
        ver(arr, b)
        cross(arr, b)
    print('#{} {} {}'.format(t, minV, min_b))