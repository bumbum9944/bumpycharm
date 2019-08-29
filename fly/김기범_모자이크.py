T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    if (r-i) % 2 == 0 and (c-j) % 2 == 1:
                        temp += arr[r][c]
                    elif (r-i) % 2 == 1 and (c-j) % 2 == 0:
                        temp += arr[r][c]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))