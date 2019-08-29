import sys
sys.stdin = open('input2.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = -1000
    sell = nums[-1]
    for i in range(len(nums)-1, -1, -1):
        if nums[i] >= sell and i != 0:
            sell = nums[i]
            continue
        profit = sell - nums[i]
        if profit > ans:
            ans = profit
    print('#{} {}'.format(tc, ans))
    # for i in range(len(nums)-1):
    #     buy = nums[i]
    #     maxv = 0
    #     for j in range(i+1,len(nums)):
    #         if nums[j] > maxv:
    #             maxv = nums[j]
    #     profit = maxv - buy
    #     if profit > ans:
    #         ans = profit
    # print('#{} {}'.format(tc, ans))
