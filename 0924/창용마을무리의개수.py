def rep(n):
    while n != p[n]:
        n = p[n]
    return n

def union(c1, c2):
    a = rep(c1)
    b = rep(c2)
    if a != b:
        p[b] = a


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [num for num in range(N+1)]
    edge = [list(map(int, input().split())) for _ in range(M)]
    for e in edge:
        union(e[0], e[1])
    cnt = 0
    for i in range(1,N+1):
        if i == p[i]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
