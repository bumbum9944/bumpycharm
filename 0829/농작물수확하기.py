T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [[int(num) for num in input()] for _ in range(N)]
    profit = 0
    for i in range(N//2+1):
        for j in range(N//2-i, N//2+1+i):
            profit += farm[i][j]
    for r in range(N//2+1,N):
        for c in range(N//2-(N-1-r), N//2+(N-1-r)+1):
            profit += farm[r][c]
    print('#{} {}'.format(tc, profit))