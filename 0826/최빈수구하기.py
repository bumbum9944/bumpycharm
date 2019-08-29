T = int(input())
for i in range(T):
    a = [0] * 101
    tc = input()
    scores = input().split()
    for score in scores:
        a[int(score)] += 1
    s_max = 0
    for idx in range(len(a)):
        if a[idx] >= s_max:
            s_max = a[idx]
            i_max = idx
    print('#{} {}'.format(tc, i_max))