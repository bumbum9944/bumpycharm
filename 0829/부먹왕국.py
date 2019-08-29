T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    gateway =list(map(int, input().split()))
    ans = 0
    for i in range(len(gateway)):
        if gateway[i] == 0:
            cnt = 0
            for j in range(i+1, i+D):
                if gateway[j] == 1:
                    cnt += 1
            if cnt == 0:
                gateway[i] = 1
                ans += 1
    print('#{} {}'.format(tc, ans))