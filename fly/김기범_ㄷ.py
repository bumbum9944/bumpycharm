T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += arr[i][j+k]
                temp += arr[i+k][j]
                temp += arr[i+M-1][j+k]
            temp -= arr[i+M-1][j]
            temp -= arr[i][j]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))