T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    print('#{}'.format(tc))
    z = ''
    for a in arr:
        for i in range(int(a[1])):
            if len(z) != 10:
                z += a[0]
            if len(z) == 10:
                print(z)
                z = ''
    if len(z) != 10:
        print(z)