T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]
    maxs = []
    for i in range(N):
        maxV = 0
        for j in range(N-M+1):
            check = honeys[i][j:j+M]
            for p in range(1, 1<<M):
                s = 0
                ss = 0
                for q in range(M):
                    if p & (1<<q) != 0 and s+check[q] <= C:
                        s += check[q]
                        ss += check[q]*check[q]
                if maxV < ss:
                    maxV = ss
        maxs.append(maxV)
    max_1 = max(maxs)
    maxs.remove(max_1)
    max_2 = max(maxs)
    ans = max_1 + max_2
    print('#{} {}'.format(tc, ans))