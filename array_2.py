arr = [[0]*4 for i in range(4)]
k = 1
# 행과 열이 같은 칸을 기준으로 오른쪽 영역
for i in range(4):
    for j in range(4):
        if i < j:
            arr[i][j] = k
            k = k + 1
print(arr)

# 행과 열이 같은 칸을 기준으로 왼쪽 영역

for i in range(4):
    for j in range(4):
        if i > j:
            arr[i][j] = k
            k = k + 1
print(arr)