T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        j = 0
        while j <= N-K:
            temp = 0
            for k in range(j, N):
                if arr[i][k] == 1:
                    temp += 1
                else:
                    j = k + 1
                    break
            if temp == K:
                cnt += 1
                j = k + 1
            elif k == N-1:
                break
        j = 0
        while j <= N-K:
            temp = 0
            for k in range(j, N):
                if arr[k][i] == 1:
                    temp += 1
                else:
                    j = k + 1
                    break
            if temp == K:
                cnt += 1
                j = k + 1
            elif k == N-1:
                break
    print('#{} {}'.format(tc, cnt))