def perm(n, s, k):
    global minV, arr, used
    if s > minV:
        return
    if n == k:
        if minV > s:
            minV = s
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                perm(n+1, s+arr[n][i], k)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    minV = 100*N
    perm(0, 0, N)
    print('#{} {}'.format(tc, minV))