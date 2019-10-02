def shoot(start, f, N, M, D):
    di = [0, -1, 0]
    dj = [-1, 0, 1]
    q = []
    ti = N - 1
    tj = start
    if f[ti][tj] != 0:
        f[ti][tj] += 1
        return
    else:
        visited = [[0]*M for _ in range(N)]
        visited[ti][tj] = 1
        q.append([ti, tj])
        while len(q) != 0:
            t = q.pop(0)
            i, j = t[0], t[1]
            for d in range(3):
                ni = i + di[d]
                nj = j + dj[d]
                if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0 and visited[i][j] < D:
                    if f[ni][nj] != 0:
                        f[ni][nj] += 1
                        return
                    else:
                        visited[ni][nj] = visited[i][j] + 1
                        q.append([ni, nj])


def defence(a1, a2, a3, N, M, D):
    kill = 0
    f = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            f[i][j] = field[i][j]
    for i in range(N):
        shoot(a1, f, N, M, D)
        shoot(a2, f, N, M, D)
        shoot(a3, f, N, M, D)
        for i in range(N):
            for j in range(M):
                if f[i][j] >= 2:
                    f[i][j] = 0
                    kill += 1

        for i in range(N-1, 0, -1):
            f[i] = f[i-1][:]
        for i in range(M):
            f[0][i] = 0
    return kill




N, M, D = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            temp = defence(i, j, k, N, M, D)
            if temp > maxV:
                maxV = temp
print(maxV)