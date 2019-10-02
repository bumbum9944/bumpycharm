def escape(i, j):
    global maze
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    if maze[i][j] == '3':
        return 1
    else:
        maze[i][j] = '1'
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni >= 0 and ni < 16 and nj >= 0 and nj < 16 and maze[ni][nj] != '1':
                if escape(ni, nj) == 1:
                    return 1
        return 0

for _ in range(10):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]
    chk = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si = i
                sj = j
    ans = escape(si, sj)
    print('#{} {}'.format(tc, ans))