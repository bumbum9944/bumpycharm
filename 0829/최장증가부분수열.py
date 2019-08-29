def f(nums, N):
    s = []
    # 출발
    i = 0
    s.append(i)
    nums[i] = 0
    cnt = 1
    while len(s) != 0:
        ti = s.pop()
        for j in raneg(i+1,N):
            if nums[ti+1] > nums[ti] and nums[ti+1] != 0:
                ti = ti + 1
                s.append(ti)
                cnt += 1
            else:
                ti += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = f(nums)