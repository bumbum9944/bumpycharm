import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a_list = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            ai = 0
            aj = 0
            if arr[i][j] != 0:
                for c in range(j,N):
                    if arr[i][c] != 0:
                        aj += 1
                    else:
                        break
                for r in range(i, N):
                    if arr[r][j] != 0:
                        ai += 1
                    else:
                        break
                for r in range(i, i+ai):
                    for c in range(j, j+aj):
                        if r >= 0 and r < N and c >= 0 and c < N:
                            arr[r][c] = 0
                a_list.append([ai, aj])
                cnt += 1
    a_list.sort(key=lambda x: [x[0]*x[1], x[0]])
    print('#{} {}'.format(tc, cnt), end=' ')
    for a in a_list:
        print('{} {}'.format(a[0], a[1]), end=' ')
    print()