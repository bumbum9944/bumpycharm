T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    p = []
    for i in range(N):
        if len(p) > 1:
            q = [1]
            for j in range(len(p)-1):
                q += [p[j] + p[j+1]]
            p = q
        p += [1]
        for k in p:
            print(k, end=' ')
        print()


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print('#{}'.format(tc))
    for i in range(N)
        for j in range(i+1)
            print(arr[i][j], end=' ')
        print()
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(arr[i][j], end=' ')
        print()
"""