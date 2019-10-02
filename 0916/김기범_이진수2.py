T = int(input())
for tc in range(1, T+1):
    N = float(input())
    nums = ''
    while N != 0 and len(nums) < 13:
        if N * 2 >= 1:
            nums += '1'
            N = N * 2 - 1
        elif N * 2 < 1:
            nums += '0'
            N = N * 2
    if len(nums) > 12:
        nums = 'overflow'
    print('#{} {}'.format(tc, nums))