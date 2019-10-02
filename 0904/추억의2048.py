# 벽으로 밀기
def move(N, S):
    global arr
    nN = int(N)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    s = ['up', 'down', 'left', 'right']
    if S == 'up':
        for r in range(nN):
            for c in range(nN):
                if arr[r][c] != 0:
                    nr = r + di[s.index(S)]
                    nc = c + dj[s.index(S)]
                    if nr >= 0 and nr < nN and nc >= 0 and nc < nN:
                        if arr[nr][nc] == 0:
                            while arr[nr][nc] == 0:
                                nr = nr + di[s.index(S)]
                                nc = nc + dj[s.index(S)]
                                if nr < 0 or nr >= nN or nc < 0 or nc >= nN:
                                    break
                            if nr >= 0 and nr < nN and nc >= 0 and nc < nN and arr[nr][nc] == arr[r][c]:
                                arr[r][c] = 0
                                arr[nr][nc] = str(arr[nr][nc] * 2)
                            else:
                                arr[nr-di[s.index(S)]][nc - dj[s.index(S)]] = arr[r][c]
                                arr[r][c] = 0
                        elif arr[nr][nc] == arr[r][c]:
                            arr[r][c] = 0
                            arr[nr][nc] = str(arr[nr][nc]*2)
    elif S == 'down':
        for r in range(nN-1,-1,-1):
            for c in range(nN):
                if arr[r][c] != 0:
                    nr = r + di[s.index(S)]
                    nc = c + dj[s.index(S)]
                    if nr >= 0 and nr < nN and nc >= 0 and nc < nN:
                        if arr[nr][nc] == 0:
                            while arr[nr][nc] == 0:
                                nr = nr + di[s.index(S)]
                                nc = nc + dj[s.index(S)]
                                if nr < 0 or nr >= nN or nc < 0 or nc >= nN:
                                    break
                            if nr >= 0 and nr < nN and nc >= 0 and nc < nN and arr[nr][nc] == arr[r][c]:
                                arr[r][c] = 0
                                arr[nr][nc] = str(arr[nr][nc] * 2)
                            else:
                                arr[nr-di[s.index(S)]][nc - dj[s.index(S)]] = arr[r][c]
                                arr[r][c] = 0
                        elif arr[nr][nc] == arr[r][c]:
                            arr[r][c] = 0
                            arr[nr][nc] = str(arr[nr][nc]*2)
    elif S == 'left':
        for c in range(nN):
            for r in range(nN):
                if arr[r][c] != 0:
                    nr = r + di[s.index(S)]
                    nc = c + dj[s.index(S)]
                    if nr >= 0 and nr < nN and nc >= 0 and nc < nN:
                        if arr[nr][nc] == 0:
                            while arr[nr][nc] == 0:
                                nr = nr + di[s.index(S)]
                                nc = nc + dj[s.index(S)]
                                if nr < 0 or nr >= nN or nc < 0 or nc >= nN:
                                    break
                            if nr >= 0 and nr < nN and nc >= 0 and nc < nN and arr[nr][nc] == arr[r][c]:
                                arr[r][c] = 0
                                arr[nr][nc] = str(arr[nr][nc] * 2)
                            else:
                                arr[nr-di[s.index(S)]][nc - dj[s.index(S)]] = arr[r][c]
                                arr[r][c] = 0
                        elif arr[nr][nc] == arr[r][c]:
                            arr[r][c] = 0
                            arr[nr][nc] = str(arr[nr][nc]*2)
    elif S == 'right':
        for c in range(nN-1, -1, -1):
            for r in range(nN):
                if arr[r][c] != 0:
                    nr = r + di[s.index(S)]
                    nc = c + dj[s.index(S)]
                    if nr >= 0 and nr < nN and nc >= 0 and nc < nN:
                        if arr[nr][nc] == 0:
                            while arr[nr][nc] == 0:
                                nr = nr + di[s.index(S)]
                                nc = nc + dj[s.index(S)]
                                if nr < 0 or nr >= nN or nc < 0 or nc >= nN:
                                    break
                            if nr >= 0 and nr < nN and nc >= 0 and nc < nN and arr[nr][nc] == arr[r][c]:
                                arr[r][c] = 0
                                arr[nr][nc] = str(arr[nr][nc] * 2)
                            else:
                                arr[nr-di[s.index(S)]][nc - dj[s.index(S)]] = arr[r][c]
                                arr[r][c] = 0
                        elif arr[nr][nc] == arr[r][c]:
                            arr[r][c] = 0
                            arr[nr][nc] = str(arr[nr][nc]*2)

T = int(input())
for tc in range(1, T+1):
    N, S = list(input().split())
    arr = [list(map(int, input().split())) for _ in range(int(N))]
    move(N, S)
    print('#{}'.format(tc))
    for i in range(int(N)):
        for j in range(int(N)):
            print(arr[i][j], end=' ')
        print()