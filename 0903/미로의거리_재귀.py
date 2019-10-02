def f(i, j, s, N):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    global minV
    if maze[i][j] == 3:
        if minV > s:# 도착지면
            minV = s
    else: # 도착지가 아니면
        maze[i][j] = 1 # 현재 칸에 방문 표시 (진행 방향에서 다시 들어오는 것 방지)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N and maze[ni][nj] != 1:
                f(ni, nj, s+1, N)
        maze[i][j] = 0 # 새로운 경로로 현재칸에 진입허용


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(num) for num in input()] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                break
        if maze[i][j] == 2:
            break
    minV = N*N
    f(si, sj, 0, N)
    if minV == N*N:
        minV = 1
    print('#{} {}'.format(tc, minV-1))