T = 10
for tc in range(1, T+1):
    K = int(input())
    nums = list(map(int, input().split()))
    for i in range(K):
        maxn = max(nums)
        maxi = nums.index(maxn)
        minn = min(nums)
        mini = nums.index(minn)
        nums[maxi] = nums[maxi] -1
        nums[mini] = nums[mini] + 1
        if maxn - minn <= 1:
            break
    ans = maxn - minn
    print('#{} {}'.format(tc, ans))