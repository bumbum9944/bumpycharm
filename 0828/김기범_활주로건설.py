def airplane(N, X, arr):
    check = [0]*N
    for i in range(N-1):
        if arr[i] != arr[i+1]:
            if arr[i+1] - arr[i] == 1:
                for x in range(i,i-X, -1):
                    if x >= 0 and arr[x] == arr[i] and check[x] == 0:
                        check[x] = 1
                    else:
                        return False
            elif arr[i+1] - arr[i] == -1:
                for x in range(i+1,i+X+1):
                    if x < N and arr[x] == arr[i+1] and check[x] == 0:
                        check[x] = 1
                    else:
                        return False
            else:
                return False
    return 1

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    cnt = 0
    field = [list(map(int, input().split())) for _ in range(N)]
    field2 = list(zip(*field))
    for arr in field:
        if airplane(N, X, arr):
            cnt += airplane(N, X, arr)
    for arr2 in field2:
        if airplane(N, X, arr2):
            cnt += airplane(N, X, arr2)
    print('#{} {}'.format(tc, cnt))