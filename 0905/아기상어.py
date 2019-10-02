def shark(i, j, size, time, time_record):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    global space
    queue = []
    time_record[i][j] = time
    queue.append([i, j])
    while len(queue) != 0:
        t = queue.pop(0)
        ti = t[0]
        tj = t[1]
        for d in range(4):
            ni = ti + di[d]
            nj = tj + dj[d]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if space[ni][nj] <= size and time_record[ni][nj] == 0:
                    queue.append([ni, nj])
                    time_record[ni][nj] = time_record[ti][tj] + 1
                    time = time_record[ni][nj]
    minV = 1000000
    idx = []
    for r in range(N):
        for c in range(N):
            if 0 < space[r][c] < size and time_record != 0:
                if minV > time_record[r][c]:
                    minV = time_record[r][c]
                    idx = [r, c]
                elif minV == time_record[r][c]:
                    if idx[0] > r:
                        idx = [r, c]
                    elif idx[0] == r:
                        if idx[1] > c:
                            idx = [r, c]
    if idx:
        space[i][j] = 0
        space[r][c] = 9
        return r, c, time
    return 0



N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
size = 2
time = 1

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            start_i = i
            start_j = j
while True:
    time_record = [[0] * N for _ in range(N)]
    if shark(start_i, start_j, size, time, time_record):
        start_i, start_j, time = shark(start_i, start_j, size, time, time_record)
        cnt += 1
        if cnt == size:
            size += 1
    else:
        break
print(time-1)
