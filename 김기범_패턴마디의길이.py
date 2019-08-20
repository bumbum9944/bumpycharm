T = int(input())
for tc in range(1, T+1):
    st = input()
    for i in range(1, 31):
        if st[0:i] == st[i:2*i]:
            cnt = len(st[0:i])
            check = list(range(i, 30, cnt))
            for j in check:
                if st[j:j+i] != st[0:i]:
                    j += 1
                    break
            if cnt >= len(st[j:]):
                break
    print('#{} {}'.format(tc, cnt))