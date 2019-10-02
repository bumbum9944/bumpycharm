T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(K)]
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]
    for _ in range(M):
        for cell in cells:
            ni = cell[0] + di[cell[3]]
            nj = cell[1] + dj[cell[3]]
            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                cell[0] = ni
                cell[1] = nj
                cell[2] = cell[2] // 2
                if cell[3] % 2:
                    cell[3] += 1
                else:
                    cell[3] -= 1
            else:
                field[ni][nj] += 1
                cell[0] = ni
                cell[1] = nj
        i = 0
        while i < len(cells)-1:
            j = i + 1
            temp = []
            while j < len(cells):
                if cells[i][0] == cells[j][0] and cells[i][1] == cells[j][1]:
                    temp.append(cells.pop(j))
                    j -= 1
                j += 1
            if temp:
                temp.append(cells[i])
                temp.sort(key=lambda x: x[2])
                s = 0
                for k in temp:
                    s += k[2]
                cells[i][2] = s
                cells[i][3] = temp[-1][3]
            i += 1
    ans = 0
    for c in cells:
        ans += c[2]
    print('#{} {}'.format(tc, ans))