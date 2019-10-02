def permutation(n, k, p):
    if n == k:
        for pp in p:
            print(pp, end=' ')
        print()
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                permutation(n+1, k, p+str(num[i]))
                visited[i] = 0

N = int(input())
num = list(range(1, N+1))
visited = [0] * (N)
permutation(0, N, '')