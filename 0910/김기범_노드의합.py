def f(n, last):
    if n <= last:
        if tree[n] == 0:
            f(n*2, last)
            f(n*2+1, last)
        tree[n//2] += tree[n]
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    leaf_set = [list(map(int, input().split())) for _ in range(M)]
    tree = [0]*(N+1)
    for leaf in leaf_set:
        tree[leaf[0]] = leaf[1]
    f(1, N)
    print('#{} {}'.format(tc, tree[L]))