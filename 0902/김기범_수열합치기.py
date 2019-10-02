T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(M)]
    base = arrs[0]
    for arr in arrs[1:]:
        start = arr[0]
        check = 0
        if len(base) > 10:
            base = [max(base[:-10])] + base[-10:]
        for i in range(len(base)):
            if base[i] > start:
                base = base[:i] + arr + base[i:]
                check += 1
                break
        if check == 0:
            base = base + arr
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(base[len(base)-1-i], end=' ')
    print()