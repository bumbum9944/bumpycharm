def bisearch(p, pp):
    left = 1
    right = p
    count = 0
    while left <= right:
        center = (left +right) // 2
        if center == pp:
            count += 1
            return count
        elif center > pp:
            right = center
            count += 1
        else:
            left = center
            count += 1
    return count

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A = bisearch(P, Pa)
    B = bisearch(P, Pb)
    if A > B:
        ans = 'B'
    elif A < B:
        ans = 'A'
    else:
        ans = '0'
    print('#{} {}'.format(tc, ans))