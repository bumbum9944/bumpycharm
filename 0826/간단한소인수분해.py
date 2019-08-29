nums = [2, 3, 5, 7, 11]
T = int(input())
for tc in range(1, T+1):
    a = []
    N = int(input())
    for n in nums:
        cnt = 0
        while N % n == 0:
            N = N // n
            cnt += 1
        a.append(cnt)
    print('#{}'.format(tc), end=' ')
    for i in a:
        print(i, end=' ')
    print()