def f(n, last):
    if n <= last:
        f(n*2, last)
        print(tree[n], end='')
        f(n*2+1, last)
for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    tree = [0]*(N+1)
    for node in nodes:
        tree[int(node[0])] = node[1]
    print('#{}'.format(tc), end=' ')
    f(1, N)
    print()