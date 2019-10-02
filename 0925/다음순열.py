def permutation(n, k, p):
    if n == k:
        p_set.append(p)
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                permutation(n+1, k, p+[num[i]])
                visited[i] = 0

N = int(input())
cnt = 1
for i in range(1, N+1):
    cnt *= i
num = list(range(1, N+1))
target = list(map(int, input().split()))
p_set = []
visited = [0] * (N)
permutation(0, N, [])
idx = p_set.index(target)
if idx == cnt-1:
    print(-1)
else:
    for p in p_set[idx+1]:
        print(p, end=' ')