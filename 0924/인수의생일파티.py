T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    arr = [[100*10000+1]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        arr[i][i] = 0
    for i in range(M):
        x, y, c = map(int, input().split())
        arr[x][y] = c
    D = arr[X]
    V = set(range(1, N+1))
    U = {X}
    while U != V:
        B = V - U
        minV = 100*10000+1
        min_idx = 0
        for b in B:
            if minV > D[b]:
                minV = D[b]
                min_idx = b
        U.add(min_idx)
        for v in range(1, N+1):
            if arr[min_idx][v] != 0 and arr[min_idx][v] != 100*10000+1:
                D[v] = min(D[v], (D[min_idx]+arr[min_idx][v]))
    D2 = []
    for i in range(N+1):
        D2.append(arr[i][X])
    U2 = {X}
    while U2 != V:
        B = V - U2
        minV = 100*10000+1
        min_idx = 0
        for b in B:
            if minV > D2[b]:
                minV = D2[b]
                min_idx = b
        U2.add(min_idx)
        for v in range(1, N+1):
            if arr[v][min_idx] != 0 and arr[v][min_idx] != 100*10000+1:
                D2[v] = min(D2[v], (D2[min_idx]+arr[v][min_idx]))
    maxV = 0
    for i in range(1, N+1):
        temp = D[i] + D2[i]
        if temp > maxV:
            maxV = temp
    print('#{} {}'.format(tc, maxV))