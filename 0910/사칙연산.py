def f(n, last):
    ss = ['+', '-', '*', '/']
    if n <= last:
        if tree[n][0] in ss:
            a = float(f(int(tree[n][1]), last))
            b = float(f(int(tree[n][2]), last))
            if tree[n][0] == '+':
                tree[n][0] = a + b
            elif tree[n][0] == '-':
                tree[n][0] = a - b
            elif tree[n][0] == '*':
                tree[n][0] = a * b
            else:
                tree[n][0] = a / b
    return tree[n][0]



for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    tree = [0]*(N+1)
    for node in nodes:
        tree[int(node[0])] = node[1:]
    ans = int(f(1, N))
    print('#{} {}'.format(tc, ans))