def package(n, s, v, r, K):
    global maxV, N
    if v == K:
        if maxV < s:
            maxV = s
    elif v > K:
        s -= item[n-1][1]
        if maxV < s:
            maxV = s
    elif s+r < maxV:
        return
    elif n == N:
        if maxV < s:
            maxV = s
    else:
        package(n+1, s+item[n][1], v+item[n][0], r-item[n][1], K)
        package(n+1, s, v, r-item[n][1], K)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    s_max = 0
    for it in item:
        item_s = it[1]
        s_max += item_s
    package(0, 0, 0, s_max, K)
    print('#{} {}'.format(tc, maxV))