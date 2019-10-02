T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stones = list(map(int, input().split()))
    K = int(input())
    start = 0
    end = 0
    ans = 0
    for i in range(N-1):
        if stones[i+1] - stones[i] > K:
            ans = -1
            break
    if ans != -1:
        while end < N:
           if stones[end] - start <= K:
               end += 1
           else:
               start = stones[end-1]
               ans += 1
        ans += 1
    print('Case #{}'.format(tc))
    print(ans)