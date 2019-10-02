def tower(i, s):
    global minV
    global B
    global staff
    if s >= B:
        dis = s - B
        if minV > dis:
            minV = dis
    elif i == len(staff):
        return
    else:
        tower(i+1, s)
        tower(i+1, s+staff[i])


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    staff = list(map(int, input().split()))
    minV = 20*10000
    tower(0, 0)
    print('#{} {}'.format(tc, minV))