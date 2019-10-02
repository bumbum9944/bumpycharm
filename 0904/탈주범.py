def move(i, j, N, M):
    global field
    global cnt
    global L
    di_1 = [-1, 1, 0, 0]
    dj_1 = [0, 0, -1, 1]
    di_2 = [-1, 1]
    dj_2 = [0, 0]
    di_3 = [0, 0]
    dj_3 = [-1, 1]
    di_4 = [-1, 0]
    dj_4 = [0, 1]
    di_5 = [1, 0]
    dj_5 = [0, 1]
    di_6 = [1, 0]
    dj_6 = [0, -1]
    di_7 = [-1, 0]
    dj_7 = [0, -1]
    di_list = [di_1, di_2, di_3, di_4, di_5, di_6, di_7]
    dj_list = [dj_1, dj_2, dj_3, dj_4, dj_5, dj_6, dj_7]
    d_1 = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
    d_2 = [[1, 2, 5, 6], [1, 2, 4, 7]]
    d_3 = [[1, 3, 4, 5], [1, 3, 6, 7]]
    d_4 = [[1, 2, 5, 6], [1, 3, 6, 7]]
    d_5 = [[1, 2, 4, 7], [1, 3, 6, 7]]
    d_6 = [[1, 2, 4, 7], [1, 3, 4, 5]]
    d_7 = [[1, 2, 5, 6], [1, 3, 4, 5]]
    dds = [d_1, d_2, d_3, d_4, d_5, d_6, d_7]
    q = []
    visited[i][j] = 1
    if visited[i][j] == L:
        return 0
    q.append([i, j])
    while len(q) != 0:
        i, j = q.pop(0)
        di = di_list[field[i][j]-1]
        dj = dj_list[field[i][j] - 1]
        dd = dds[field[i][j] - 1]
        for d in range(len(di)):
            ni = i + di[d]
            nj = j + dj[d]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0 and field[ni][nj] != 0 and (field[ni][nj] in dd[d]):
                visited[ni][nj] = visited[i][j] + 1
                if visited[ni][nj] > L:
                    visited[ni][nj] = 0
                    return 0
                q.append([ni, nj])


def f_cnt():
    global visited
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N, M , si, sj, L = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    move(si, sj, N, M)
    ans = f_cnt()
    print('#{} {}'.format(tc, ans))