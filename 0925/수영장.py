def plan_maker(n, s):
    global minV, d, m, m3, plan
    if n >= 13:
        if minV > s:
            minV = s
    else:
        plan_maker(n+1, s + plan[n]*d)
        plan_maker(n+1, s + m)
        plan_maker(n+3, s + m3)

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    minV = y
    plan_maker(0, 0)
    print('#{} {}'.format(tc, minV))