def f(n, last):
    if n <= last:
        if tree[n//2] > tree[n]:
            tree[n//2], tree[n] = tree[n], tree[n//2]
            f(n//2, last)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (N+1)
    for i in range(N):
        tree[i+1] = nums[i]
        f(i+1, N)
    s = 0
    last = N
    while last > 0:
        last = last // 2
        s += tree[last]

    print('#{} {}'.format(tc, s))