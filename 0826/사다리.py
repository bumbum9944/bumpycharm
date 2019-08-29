import sys
sys.stdin = open('input.txt', 'r')
di = [0, 0]
dj = [1, -1]
for t in range(10):
    q = []
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    ti = 99
    for j in range(100):
        if ladder[ti][j] == 2:
            tj = j
    q.append([ti, tj])
    while ti > 0:
        t = q.pop(0)
        ti = t[0]
        tj = t[1]
        for k in range(2):
            ni = ti + di[k]
            nj = tj + dj[k]
            if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] == 1:
                q.append([ni, nj])
                ladder[ni][nj] = 0
        if len(q) == 0:
            ni = ti - 1
            nj = tj
            if ni >= 0 and ni < 99:
                q.append([ni, nj])
                ladder[ni][nj] = 0
    print('#{} {}'.format(tc, tj))