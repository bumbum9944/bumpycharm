T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):
        f = nums.pop(0)
        nums.append(f)
    print('#{} {}'.format(tc, nums[0]))