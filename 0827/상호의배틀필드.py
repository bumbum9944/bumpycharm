import sys
sys.stdin = open('input.txt', 'r')
def move(ipr, ipc, command):
    global H
    global W
    global field
    # 전차의 방향 바꾸기
    commands = ['U', 'D', 'L', 'R']
    points = ['^', 'v', '<', '>']
    dir_i = [-1, 1, 0, 0]
    dir_j = [0, 0, -1, 1]
    c = command
    field[ipr][ipc] = points[commands.index(c)]
    # 지면인지 확인하고 한칸 이동
    if ipr+dir_i[commands.index(c)] >= 0 and ipr+dir_i[commands.index(c)] < H and ipc+dir_j[commands.index(c)] >= 0 and ipc+dir_j[commands.index(c)] < W and field[ipr+dir_i[commands.index(c)]][ipc+dir_j[commands.index(c)]] == '.':
        field[ipr][ipc] = '.'
        field[ipr+dir_i[commands.index(c)]][ipc+dir_j[commands.index(c)]] = points[commands.index(c)]
        ipr = ipr+dir_i[commands.index(c)]
        ipc = ipc+dir_j[commands.index(c)]
        return ipr, ipc
    else:
        return ipr, ipc
#s는 쏜다
# 포탄은 맵 끝까지 날아가서 사라짐
def shoot(ipr, ipc):
    points = ['^', 'v', '<', '>']
    dir_r = [-1, 1, 0, 0]
    dir_c = [0, 0, -1, 1]
    global field
    global H
    global W
    ti = ipr
    tj = ipc
    while True:
        nr = ti + dir_r[points.index(field[ipr][ipc])]
        nc = tj + dir_c[points.index(field[ipr][ipc])]
        if nr >= 0 and nr < H and nc >= 0 and nc < W:
# 벽이 강철이면 아무일도 없음
            ti = nr
            tj = nc
            if field[nr][nc] == '#':
                break
# 벽이 벽돌집이면 지면으로 바뀜
            elif field[nr][nc] == '*':
                field[nr][nc] = '.'
                break
        else:
            break

cmdm = ['U', 'D', 'L', 'R']
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    cmd = input()
#전차의 초기 위치를 찾자
    tank = ['<', '>', '^', 'v']
    for r in range(H):
        for c in range(W):
            if field[r][c] in tank:
                ipr = r
                ipc = c
                break
    for cd in cmd:
        if cd not in cmdm:
            shoot(ipr, ipc)
        else:
            ipr, ipc = move(ipr, ipc, cd)
    print('#{}'.format(tc), end=' ')
    for k in field:
        print(''.join(k))