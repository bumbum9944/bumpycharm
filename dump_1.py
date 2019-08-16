import sys
sys.stdin = open('input.txt', 'r')

T = 10
K = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    cnt = 0
    gap = 100
    print(len(nums))
    # while gap > 1:
    #     maxi = 0
    #     mini = 0
    #     for i in range(1, 100):
    #         if nums[i] > nums[maxi]:
    #             maxi = i
    #         if nums[i] < nums[mini]:
    #             mini = i
    #     gap = nums[maxi] - nums[mini]
    #     if gap <= 1:
    #         break
    #     else:
    #         nums[maxi] -= 1
    #         nums[mini] += 1
    #         cnt += 1
    # print('# {} {}'.format(tc, cnt))

