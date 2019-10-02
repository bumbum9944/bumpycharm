def zero_find(field):
    global di,dj,N
    for i in range(N):
        for j in range(N):
            if field[i][j] == '.':
                cnt = 0
                for d in range(8):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if ni >= 0 and ni < N and nj >= 0 and nj < N and field[ni][nj] != 0:
                        if field[ni][nj] == '*':
                            cnt = 1
                            break
                if cnt == 0:
                    field[i][j] = 0
                    for d in range(8):
                        ni = i + di[d]
                        nj = j + dj[d]
                        if ni >= 0 and ni < N and nj >= 0 and nj < N and field[ni][nj] != 0:
                            field[ni][nj] = 0

def zero_count(field):
    global N
    global ans
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    queue = []
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                queue.append([i,j])
                while len(queue) != 0:
                    t = queue.pop(0)
                    ti, tj = t[0], t[1]
                    field[ti][tj] = 1
                    for d in range(4):
                        ni = ti + di[d]
                        nj = tj + dj[d]
                        if ni >= 0 and ni < N and nj >= 0 and nj < N:
                            if field[ni][nj] == 0:
                                queue.append([ni, nj])
                ans += 1
def bomb_count(field):
    global N
    global ans
    for i in range(N):
        for j in range(N):
            if field[i][j] == '.':
                ans += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    ans = 0
    zero_find(field)
    zero_count(field)
    bomb_count(field)
    print('#{} {}'.format(tc, ans))