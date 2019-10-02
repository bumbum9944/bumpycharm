# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    arr = [[0]*201 for _ in range(201)]
    j = 1
    num = 1
    for i in range(1, 201):
        while i != 0:
            arr[i][j] = num
            if num == 10000:
                break
            num += 1
            i -= 1
            j += 1
        if num == 10000:
            break
        j = 1
    idx_list = []
    check = [p, q]
    for c in check:
        for i in range(1,201):
            for j in range(1, 201):
                if arr[i][j] == c:
                    idx_list.append([i, j])
    idx = [idx_list[0][0] + idx_list[1][0], idx_list[0][1] + idx_list[1][1]]
    start_num = 0
    for i in range(idx[1]):
        start_num += i+1
    v = i+1
    for j in range(idx[0]-1):
        start_num += v
        v += 1
    print('#{} {}'.format(tc, start_num))