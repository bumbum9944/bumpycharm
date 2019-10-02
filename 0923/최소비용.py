def plan(r, c, visited):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    queue = []
    visited[r][c] = 0
    queue.append([r, c])
    while len(queue) != 0:
        t = queue.pop(0)
        i = t[0]
        j = t[1]
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if arr[ni][nj] > arr[i][j]:
                    if visited[ni][nj] > visited[i][j] + 1 + (arr[ni][nj] - arr[i][j]):
                        visited[ni][nj] = visited[i][j] + 1 + (arr[ni][nj] - arr[i][j])
                        queue.append([ni, nj])
                else:
                    if visited[ni][nj] > visited[i][j] + 1:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append([ni, nj])
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1000*N]*N for _ in range(N)]
    ans = plan(0, 0, visited)
    print('#{} {}'.format(tc, ans))