def bfs(voter, N):
    q = []
    q.append(voter[0])
    v = [0] * (N+1)
    v[voter[0]] = 1
    total = 0
    while len(q) != 0:
        i = q.pop(0)
        total += p[i]
        for j in voter:
            if arr[i][j] == 1 and v[j] == 0:
                q.append(j)
                v[j] = 1
    for i in voter:
        if v[i] == 0:
            return 0
    return total

N = int(input())
p = [0] + list(map(int, input().split()))
arr = [[0]*(N+1) for _ in range(N+1)]
minV = 10000000
for i in range(1, N+1):
    area = list(map(int, input().split()))
    for j in area[1:]:
        arr[i][j] = 1
        arr[j][i] = 1

for i in range(1, (1<<N)//2):
    A = []
    B = []
    for j in range(N):
        if i & (1<<j) != 0:
            A.append(j+1) # j + 1을 선거구 번호로 활용
        else:
            B.append(j+1)
    a = bfs(A, N)
    b = bfs(B, N)
    if a != 0 and b != 0:
       c = abs(a-b)
       if minV > c:
           minV = c
if minV == 10000000:
   minV = -1
print(minV)