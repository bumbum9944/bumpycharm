def rep(n):
    while p[n] != n:
        n = p[n]
    return n

def union(n1, n2, w):
    global s, p
    p1 = rep(n1)
    p2 = rep(n2)
    if p1 != p2:
        p[p2] = p1
        s += w

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x : x[2])
    p = list(range(V+1))
    s = 0
    for edge in edges:
        n1 = edge[0]
        n2 = edge[1]
        w = edge[2]
        union(n1, n2, w)
    print('#{} {}'.format(tc, s))