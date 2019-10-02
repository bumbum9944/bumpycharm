T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        t1, t2 = map(int, input().split())
        arr[t1][t2] = 1
        arr[t2][t1] = 1
    friend = []
    for i in range(1, N+1):
        if arr[1][i] != 0:
            friend.append(i)
    friend2 = friend[:]
    for f in friend:
        for j in range(1, N + 1):
            if arr[f][j] != 0 and j not in friend2 and j != 1:
                friend2.append(j)
    print('#{} {}'.format(tc, len(friend2)))