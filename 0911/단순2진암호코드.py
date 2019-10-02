T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    password = []
    num = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4],
           [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    ai = 0
    aj = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if int(arr[i][j]) == 1:
                ai = i
                aj = j
                break
        if ai != 0:
            break
    arr_t = arr[ai][aj-55:aj+1]
    for a in range(0, 56, 7):
        cnt0 = 0
        cnt1 = 0
        a0 = []
        a1 = []
        for i in range(a, a+7):
            if int(arr_t[i]) == 0:
                if cnt1 != 0:
                    a1.append(cnt1)
                    cnt1 = 0
                cnt0 += 1
            else:
                if cnt0 != 0:
                    a0.append(cnt0)
                    cnt0 = 0
                cnt1 += 1
        a1.append(cnt1)

        code = []
        for i in range(2):
            code.append(a0[i])
            code.append(a1[i])

        password.append(num.index(code))
    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += password[i]
        else:
            even += password[i]
    password_t = odd*3 + even
    ans = 0
    if password_t % 10 == 0:
        ans = sum(password)
    print('#{} {}'.format(tc, ans))


