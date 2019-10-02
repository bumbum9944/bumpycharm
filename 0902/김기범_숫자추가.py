T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    idx_num = [list(map(int, input().split())) for _ in range(M)]
    for i in idx_num:
        idx = i[0]
        num = i[1]
        nums = nums[:idx]+[num]+nums[idx:]
    print('#{} {}'.format(tc, nums[L]))