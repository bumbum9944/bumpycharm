def permutation(c, k, s):
    global cases, idx, used, minV
    if s > minV:
        return
    if c == k:
        if minV > s:
            minV = s
    else:
        for i in range(len(idx)):
            if used[i] == 0:
                used[i] = 1
                permutation(c+1, k, s+abs(area[i][0] - factory[c][0]) + abs(area[i][1] - factory[c][1]))
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    factory = [list(map(int, input().split())) for _ in range(N)]
    cases = []
    idx = list(range(N))
    used = [0] * N
    minV = 100 * N
    permutation(0, N, 0)
    print('#{} {}'.format(tc, minV))