import sys
sys.stdin = open('sample_input(2).txt', 'r')

def find(i, j, s, N, c):
    global longest
    global K
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visited[i][j] = 1
    if s > longest:
        longest = s
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni >= 0 and ni < N and nj >= 0 and nj < N:
            if mountain[i][j] > mountain[ni][nj]:
                find(ni, nj, s+1, N, c)
            elif mountain[i][j] > mountain[ni][nj] - K and visited[ni][nj] != 1 and c == 1:
                remember = mountain[ni][nj]
                mountain[ni][nj] = mountain[i][j] - 1
                find(ni, nj, s+1, N, c-1)
                mountain[ni][nj] = remember
    visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    longest = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > maxV:
                maxV = mountain[i][j]
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == maxV:
                find(r, c, 1, N, 1)
    print('#{} {}'.format(tc, longest))