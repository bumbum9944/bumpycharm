T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        command = list(input().split())
        if len(command) == 2:
            arr.remove(arr[int(command[1])])
        else:
            if command[0] == 'I':
                arr.insert(int(command[1]), int(command[2]))
            else:
                arr[int(command[1])] = int(command[2])
    if L >= len(arr):
        ans = -1
    else:
        ans = arr[L]
    print('#{} {}'.format(tc, ans))