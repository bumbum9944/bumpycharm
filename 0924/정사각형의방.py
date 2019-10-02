def find(r, c, visited, queue):
    global N, arr, num, maxV, min_room
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    front = rear = -1
    visited[r][c] = 1
    rear += 1
    queue[rear] = [r, c]
    while front != rear:
        front += 1
        ti = queue[front][0]
        tj = queue[front][1]
        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if arr[ni][nj] == arr[ti][tj] + 1 and visited[ni][nj] < visited[ti][tj] + 1:
                    visited[ni][nj] = visited[ti][tj] + 1
                    rear += 1
                    queue[rear] = [ni, nj]
    if maxV < visited[ti][tj]:
        maxV = visited[ti][tj]
        min_room = arr[r][c]
    elif maxV == visited[ti][tj]:
        if min_room > arr[r][c]:
            min_room = arr[r][c]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    min_room = 1
    visited = [[0] * N for _ in range(N)]
    queue = [0] * N ** 2
    for r in range(N):
        for c in range(N):
            find(r, c, visited, queue)
    print('#{} {} {}'.format(tc, min_room, maxV))