def s(arr):
    # 가로 세로 검증
    for i in range(9):
        ai = []
        aj = []
        for j in range(9):
            if arr[i][j] not in ai:
                ai.append(arr[i][j])
            if arr[j][i] not in aj:
                aj.append(arr[j][i])
        if len(ai) != 9 or len(aj) != 9:
            return 0

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            ak = []
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if arr[r][c] not in ak:
                        ak.append(arr[r][c])
            if len(ak) != 9:
                return 0
    return 1
T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(9)]
    print('#{} {}'.format(tc, s(arr)))