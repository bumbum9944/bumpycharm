T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 각 자리에서 다음 자리에 있는 숫자를 곱했을 때
    # 그 수의 자릿수들이 단조 증가를 이루면 된다

    # 각 자리 숫자는 10으로 나누어 가며 확인 가능
    maxV = -1
    for i in range(N-1):
        for j in range(i+1, N):
            target = nums[i]*nums[j]
            target_copy = target
            while target_copy != 0:
                a = target_copy % 10
                target_copy = target_copy // 10
                b = target_copy % 10
                if a < b:
                    break
            if target_copy == 0:
                if maxV < target:
                    maxV = target
    print('#{} {}'.format(tc, maxV))