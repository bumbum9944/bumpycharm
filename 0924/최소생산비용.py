def permutation(c, s, k):
    global cases, idx, used, minV
    # if s > minV:
    #     return
    if c == k:
        if minV > s:
            minV = s
    else:
        for i in range(len(idx)):
            if used[i] == 0:
                used[i] = 1
                permutation(c+1, s + cost[c][idx[i]], k)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    cases = []
    idx = list(range(N))
    used = [0] * N
    minV = 100 * N
    permutation(0, 0, N)
    print('#{} {}'.format(tc, minV))