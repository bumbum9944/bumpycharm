def swim(mon, s, d, m, m3):
    global month
    global minV
    if mon >= 13:
        if minV > s:
            minV = s
    else:
        # 1일권
        swim(mon+1, s+d*month[mon], d, m, m3)
        # 1달권
        swim(mon + 1, s + m, d, m, m3)
        # 3달권
        swim(mon + 3, s + m3, d, m, m3)

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    minV = y
    swim(1, 0, d, m, m3)
    print('#{} {}'.format(tc, minV))