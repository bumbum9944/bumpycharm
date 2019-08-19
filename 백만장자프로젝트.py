T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sell_day = num_list[-1]
    ans = 0
    for i in range(N-1):
        if num_list[N-2-i] <= sell_day:
            ans += sell_day - num_list[N-2-i]
        else:
            sell_day = num_list[N-2-i]
    print('#{} {}'.format(tc, ans))