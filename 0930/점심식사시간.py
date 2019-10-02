T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = []
    p = []
    minV = 100000000000000
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                p.append([i, j])
            elif arr[i][j] != 0 and arr[i][j] != 1:
                s.append([i, j])
    dis = []
    for i in p:
        temp = []
        for j in range(2):
            temp.append(abs(i[0]-s[j][0]) + abs(i[1]-s[j][1]))
        dis.append(temp)

    for i in range(1 << len(p)):
        s1 = []
        s2 = []
        for j in range(len(p)):
            if i & (1 << j):
                s1.append(dis[j][0])
            else:
                s2.append(dis[j][1])

        s1.sort()
        s2.sort()
        t1 = [0] * 200
        t2 = [0] * 200
        for ss1 in s1:
            for k in range(arr[s[0][0]][s[0][1]]):
                if t1[ss1+1+k] < 3:
                    t1[ss1 + 1 + k] += 1
                else:
                    tss = ss1
                    c = 0
                    while True:
                        tss += 1
                        if t1[tss + 1 + k] < 3:
                            t1[tss + 1 + k] += 1
                            c += 1
                            if c + k == arr[s[0][0]][s[0][1]]:
                                break
                    break

        for ss2 in s2:
            for k in range(arr[s[1][0]][s[1][1]]):
                if t2[ss2+1+k] < 3:
                    t2[ss2 + 1 + k] += 1
                else:
                    tss = ss2
                    c = 0
                    while True:
                        tss += 1
                        if t2[tss + 1 + k] < 3:
                            t2[tss + 1 + k] += 1
                            c += 1
                            if c + k == arr[s[1][0]][s[1][1]]:
                                break
                    break

        maxV = 0
        for i in range(199, -1, -1):
            if t1[i] != 0:
                if maxV < i+1:
                    maxV = i+1
            if t2[i] != 0:
                if maxV < i+1:
                    maxV = i+1
        if minV > maxV:
            minV = maxV
    print('#{} {}'.format(tc, minV))