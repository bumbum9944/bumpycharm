def rot(arr):
    for i in range(N):
        for j in range(N):
            print(arr[N-1-j][i], end='')
        print(end=' ')
        for k in range(N):
            print(arr[N-1-i][N-1-k], end='')
        print(end=' ')
        for l in range(N):
            print(arr[l][N-1-i], end='')
        print()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    print('#{}'.format(tc))
    rot(arr)