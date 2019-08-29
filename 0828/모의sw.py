def check(arr, arr2):
    cnt = 0
    i = 1
    point = [0, 1, 2, 3]
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    while i != 999:
        for r in range(2001):
            for c in range(2001):
                for k in range(4):
                    if point[k] == arr[r][c]:
                        nr = r + di[k]
                        nc = c + dj[k]
                        if nr >= 0 and nr < 2001 and nc >= 0 and nc < 2001:
                            if arr[nr][nc] != 4:
                                cnt += arr2[nr][nc] + arr2[r][c]
                                arr2[nr][nc] = 0
                                arr2[r][c] = 0
                                arr[nr][nc] = 4
                                arr[r][c] = 4
                            else:
                                arr[r][c] = 4
                                arr[nr][nc] = point[k]
                            break
                        else:
                            break
        i += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    arr = [[4] * 2001 for _ in range(2001)]
    arr2 = [[0] * 2001 for _ in range(2001)]
    N = int(input())
    for i in range(N):
        x, y, point, K = map(int, input().split())
        X = x + 1000
        Y = y + 1000
        arr[Y][X] = point
        arr2[Y][X] = K
    ans = check(arr, arr2)
    print('#{} {}'.format(tc, ans))