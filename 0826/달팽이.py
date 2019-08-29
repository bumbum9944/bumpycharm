di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dir = 0
    i = 0 # 현재칸 좌표
    j = 0
    k = 1 # 칸에 기록할 값
    while k <= 9: # 아직 NxN칸 이내면
        arr[i][j] = k # 현재칸에 값을 쓰고
        k += 1 # 다음 칸에 쓸 값 결정
        # 다음칸을 결정, 배열을 벗어나지 않고 비어있어야 함
        # 현재방향으로 다음칸 계산할 지, 다음 방향으로 계산할 지 결정
        ni = i+di[dir]
        nj = j+dj[dir]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1)%4
            i += di[dir]
            j += dj[dir]