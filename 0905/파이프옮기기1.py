def move(i, j, mod, N):
    global house
    global cnt
    if i == N-1 and j == N-1:
        cnt += 1
    else:
        if mod == 1:
            for d in range(2):
                if d == 1:
                    if j+1 < N and i+1 < N and house[i][j+1] == 0 and house[i+1][j+1] == 0 and house[i+1][j] == 0:
                        move(i+1, j+1, 3, N)
                    else:
                        return
                else:
                    ni = i
                    nj = j + 1
                    if ni >= 0 and ni < N and nj >= 0 and nj < N:
                        if house[ni][nj] == 1:
                            return
                        else:
                            move(ni, nj, 1, N)
        elif mod == 2:
            for d in range(2):
                if d == 1:
                    if j + 1 < N and i + 1 < N and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0 and house[i + 1][
                        j] == 0:
                        move(i+1, j+1, 3, N)
                    else:
                        return
                else:
                    ni = i + 1
                    nj = j
                    if ni >= 0 and ni < N and nj >= 0 and nj < N:
                        if house[ni][nj] == 1:
                            return
                        else:
                            move(ni, nj, 2, N)
        elif mod == 3:
            for d in range(3):
                if d == 2:
                    if j + 1 < N and i + 1 < N and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0 and house[i + 1][
                        j] == 0:
                        move(i+1, j+1, 3, N)
                    else:
                        return
                else:
                    di = [0, 1]
                    dj = [1, 0]
                    ni = i + di[d]
                    nj = j + dj[d]
                    if ni >= 0 and ni < N and nj >= 0 and nj < N:
                        if house[ni][nj] == 1:
                            return
                        else:
                            move(ni, nj, d+1, N)

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
i = 0
j = 1
cnt = 0
move(i, j, 1, N)
print(cnt)
