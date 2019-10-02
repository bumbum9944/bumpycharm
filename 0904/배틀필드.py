def move(i, j, H, W):



T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    tank = ['^','v','<','>']
    check = 0
    commands = input()
    for i in range(H):
        for j in range(W):
            if field[i][j] in tank:
                si = i
                sj = j
                check = 1
                break
        if check == 1:
            break

    for command in commands:
        if command == 'S':
            shoot(si, sj, H, W)
        else:
            move(si, sj, H, W)