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