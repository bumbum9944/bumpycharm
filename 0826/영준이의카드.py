def card(s):
    c_s = [0] * 14
    c_d = [0] * 14
    c_h = [0] * 14
    c_c = [0] * 14
    cards = [c_s, c_d, c_h, c_c]
    for i in range(0, len(s), 3):
        if s[i] == 'S':
            c_s[int(s[i+1:i+3])] += 1
            if c_s[int(s[i+1:i+3])] >= 2:
                return 'ERROR'
        elif s[i] == 'D':
            c_d[int(s[i+1:i+3])] += 1
            if c_d[int(s[i+1:i+3])] >= 2:
                return 'ERROR'
        elif s[i] == 'H':
            c_h[int(s[i+1:i+3])] += 1
            if c_h[int(s[i+1:i+3])] >= 2:
                return 'ERROR'
        elif s[i] == 'C':
            c_c[int(s[i+1:i+3])] += 1
            if c_c[int(s[i+1:i+3])] >= 2:
                return 'ERROR'
    ans = ''
    for c in cards:
        ans = ans + str(13-sum(c)) + ' '
    return ans

T = int(input())
for tc in range(1, T+1):
    s = input()
    print('#{} {}'.format(tc, card(s)))