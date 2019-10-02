def permutation(n, s, k):
    global minV, used
    if s > minV:
        return
    if n == k:
        if minV > s:
            minV = s
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                permutation(n+1, s+abs(area[n][0]-factory[i][0])+abs(area[n][1]-factory[i][1]), k)
                used[i] = 0

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
factory = [list(map(int, input().split())) for _ in range(N)]
minV = 1000*N
used = [0]*N
permutation(0, 0, N)
print(minV)