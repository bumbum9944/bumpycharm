T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    ans = F * time
    print('#{} {}'.format(tc, ans))