import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(100):
        i = 0
        while i < 99:
            if arr[i][j] == 1:
                for r in range(i+1, 100):
                    if arr[r][j] == 2:
                        i = r+1
                        cnt += 1
                        break
                if r == 99:
                    break
            else:
                i += 1
    print('#{} {}'.format(tc, cnt))