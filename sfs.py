def rotation(matrix):
    matrix_col90 = list(zip(*matrix))
    mat_col90 = []
    for i in range(len(matrix_col90)):
        ma_col90 = []
        for j in matrix_col90[i]:
            ma_col90 = [j] + ma_col90
        mat_col90.append(ma_col90)
    return mat_col90

tests = int(input())
for test in range(1, tests+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())))

    m90 = rotation(mat)
    m180 = rotation(m90)
    m270 = rotation(m180)
    print('#{}'.format(test))
    for i in range(N):
        for num in m90[i]:
            print('{}'.format(num), end='')
        print(' ', end='')
        for num in m180[i]:
            print('{}'.format(num), end='')
        print(' ', end='')
        for num in m270[i]:
            print('{}'.format(num), end='')
        print(' ', end='')
        print()
