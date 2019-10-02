def num_train(i, j, num_line):
    global num_lines
    global arr
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    if len(num_line) == 7:
        num_lines.add(tuple(num_line))
    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if ni >= 0 and ni < 4 and nj >= 0 and nj < 4:
                num_train(ni, nj, num_line+[arr[ni][nj]])



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    num_lines = set()
    for i in range(4):
        for j in range(4):
            num_train(i, j, [arr[i][j]])
    print('#{} {}'.format(tc, len(num_lines)))