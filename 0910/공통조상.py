def f(n, last):
    if n <= last:
        if n == nums[2] or n == nums[3]:
            return n
        else:
            a = f(n*2, last)
            b = f(n*2+1, last)
            if a != 0 and b != 0:
                return n
            else:
                return max(a, b)
    return 0
def height(n):
    p = n
    cnt = 0
    cnt2 = 0
    c1 = ch1[p]
    while c1 != 0:
        cnt += 1
        p = c1
    p = n
    c2 = ch2[p]
    while c2 != 0:
        cnt2 += 1
        p = c2
    return max(cnt, cnt2)
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    V = nums[0]
    E = nums[1]
    nn = list(map(int, input().split()))
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    tree = [0]*(V+1)
    for i in range(V-1):
        if ch1[nn[i*2]] == 0:
            ch1[nn[i*2]] = nn[i*2+1]
        else:
            ch2[nn[i * 2]] = nn[i * 2 + 1]
    for i in range(V-1):
        tree[nn[i*2]] = nn[i*2+1]
    n = f(1, V)
    ans = height(n)
    print('#{} {} {}'.format(tc, n, ans))