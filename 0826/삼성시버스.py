T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    ps = [int(input()) for _ in range(P)]
    print('#{}'.format(tc), end=' ')
    for i in ps:
        cnt = 0
        for ns in ab:
            if ns[0] <= i <= ns[1]:
                cnt += 1
        print(cnt, end=' ')
    print()