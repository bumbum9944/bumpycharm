T = int(input())
for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    box = []
    for i in s1:
        if i not in box:
            box += [i]
    ans = 0
    for j in box:
        temp = 0
        for k in s2:
            if j == k:
                temp += 1
        if ans < temp:
            ans = temp
    print('#{} {}'.format(tc, ans))