def delivery(x, y, dis, c):
    global N
    global customer_idx
    global check
    global house
    global minV
    if c == N:
        s = abs(x - house[0]) + abs(y - house[1])
        ans = dis + s
        if minV > ans:
            minV = ans
    else:
        if minV < dis:
            return
        for i in range(len(customer_idx)):
            if check[i] == 0:
                s = abs(x-customer_idx[i][0]) + abs(y-customer_idx[i][1])
                nx, ny = customer_idx[i][0], customer_idx[i][1]
                check[i] = 1
                delivery(nx, ny, dis+s, c+1)
                check[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    customer = list(map(int, input().split()))
    customer_idx = []
    temp = []
    for i in customer:
        temp.append(i)
        if len(temp) == 2:
            customer_idx.append(temp)
            temp = []
    company = customer_idx.pop(0)
    house = customer_idx.pop(0)
    check = [0]*len(customer_idx)
    x = company[0]
    y = company[1]
    minV = 2000000000000000
    delivery(x, y, 0, 0)
    print('#{} {}'.format(tc, minV))