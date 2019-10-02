T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    for i in range(K):
        if start + M > len(arr):
            a =len(arr)
            arr = arr[:start + M - len(arr)] + [arr[start + M - len(arr)-1] + arr[start + M - len(arr)]] + arr[start + M - len(arr):]
            start = start + M - a
        elif start + M == len(arr):
            arr = arr[:start + M] + [arr[- 1] + arr[0]] + arr[start + M:]
            start = start + M
        else:
            arr = arr[:start+M] + [arr[start+M-1]+arr[start+M]] + arr[start+M:]
            start = start + M
    print('#{}'.format(tc), end=' ')
    if len(arr) <= 10:
        for i in range(len(arr)):
            print(arr[len(arr)-1-i], end=' ')
    else:
        for i in range(10):
            print(arr[len(arr) - 1 - i], end=' ')
    print()