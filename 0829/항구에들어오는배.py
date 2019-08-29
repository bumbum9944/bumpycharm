T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    cnt = 0
    steps = []
    for i in range(1, N):
        steps.append((nums[i]-1))
    for k in range(len(steps)):
        if steps[k] != 'no':
            for c in range(k+1, len(steps)):
                if steps[c] != 'no' and steps[c] % steps[k] == 0:
                    steps[c] = 'no'
    for s in steps:
        if s != 'no':
            cnt += 1
    print('#{} {}'.format(tc, cnt))