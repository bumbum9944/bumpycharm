import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]
    di = [1, 1, 1, 0, -1, -1, -1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N//2-1,N//2+1):
        for j in range(N // 2 - 1, N // 2 + 1):
            if i == j:
                field[i][j] = 2
            else:
                field[i][j] = 1

    for _ in range(M):
        stone = list(map(int, input().split()))
        i = stone[1]-1
        j = stone[0]-1
        field[i][j] = stone[2]
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if ni >= 0 and ni < N and nj >= 0 and nj < N and field[ni][nj] != 0:
                if field[ni][nj] % 2 != field[i][j] % 2:
                    nni = ni + di[d]
                    nnj = nj + dj[d]
                    check = 0
                    while nni >= 0 and nni < N and nnj >= 0 and nnj < N and field[nni][nnj] != 0 and field[nni][nnj] != field[i][j]:
                        nni = nni + di[d]
                        nnj = nnj + dj[d]
                        check += 1
                    if nni >= 0 and nni < N and nnj >= 0 and nnj < N and field[nni][nnj] == field[i][j]:
                        for ch in range(check+1):
                            field[ni][nj] = field[i][j]
                            ni = ni + di[d]
                            nj = nj + dj[d]
    cnt_1 = 0
    cnt_2 = 0
    for r in range(N):
        for c in range(N):
            if field[r][c] == 1:
                cnt_1 += 1
            elif field[r][c] == 2:
                cnt_2 += 1
    print('#{} {} {}'.format(tc, cnt_1, cnt_2))