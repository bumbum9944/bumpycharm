T = int(input())
for tc in range(1, T+1):
    ans = -1
    N = int(input())
    nums = list(map(int, input().split()))
    # 우선 주어지는 각 수들을 곱한다.
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            check = 0
            dan_o = nums[j]*nums[i]
            dan = dan_o
    # 곱한 값의 각 자릿수들을 다음 수와 비교해서 크거나 같으면 단조 증가
            while dan != 0:
                a = dan % 10
                dan = dan // 10
                b = dan % 10
                if a >= b:
                    continue
                else:
                    check = -1
                    break
            if check != -1:
                if dan_o > ans:
                    ans = dan_o
    print('#{} {}'.format(tc, ans))