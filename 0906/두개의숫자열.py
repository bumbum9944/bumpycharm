T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    S = list(map(int, input().split()))
    if N < M:
        L, S = S, L
        N, M = M, N
    maxV = -100000000000000000000000000000000
    for i in range(N-M+1):
        ans = 0
        for j in range(M):
            ans += L[i+j] * S[j]
        if maxV < ans:
            maxV = ans
    print('#{} {}'.format(tc, maxV))