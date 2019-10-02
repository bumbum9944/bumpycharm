def queen(i, j, N):
    global chess
    global cnt
    global ans
    di = [-1, -1, -1]
    dj = [-1, 0, 1]
    for d in range(3):
        ni = i + di[d]
        nj = j + dj[d]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and chess[ni][nj] == 0:
            while ni >= 0 and ni < N and nj >= 0 and nj < N and chess[ni][nj] == 0:
                ni = ni + di[d]
                nj = nj + dj[d]
            if chess[ni][nj] == 1:
                queen(i, j+1, N)
            else:
                chess[i][j] = 1
                cnt += 1
                if cnt == N:
                    ans += 1
                    cnt = 0
                if i+1 < N:
                    queen(i+1, 0, N)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    chess = [[0]*N for _ in range(N)]
    cnt = 0
    ans = 0
    i = 0
    for j in range(N):
        queen(i, j, N)
    print('#{} {}'.format(tc, cnt))