T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    for i in range(E):
        p = edge[i*2]
        c = edge[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    queue = []
    p = N
    cnt = 1
    queue.append(p)
    while len(queue) != 0:
        p = queue.pop(0)
        if ch1[p] != 0:
            cnt += 1
            queue.append(ch1[p])
        if ch2[p] != 0:
            cnt += 1
            queue.append(ch2[p])

    print('#{} {}'.format(tc, cnt))