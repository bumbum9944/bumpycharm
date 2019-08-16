T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = 0
    arr = [[0] * 10 for i in range(10)]
    for cn in range(N):
        color = list(map(int, input().split()))
        for i in range(color[1], color[3]+1):
            for j in range(color[0], color[2]+1):
                if arr[i][j] == 0:
                    arr[i][j] = color[-1]
                else:
                    arr[i][j] = 3
    for i in arr:
        total += i.count(3)
    print('#{} {}'.format(tc, total))