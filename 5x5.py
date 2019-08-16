"""
5x5 인 모든 칸의 이웃에 대해 조사하는 경우
모든 칸의 범위는
for i : 0 -> 4
    for j : 0 -> 4
        if (j+1 <= 4)
        if (i+1 <= 4)
        if (j-1 >= 0)
        if (i-1 >= 0)

"""
arr = [[0]*5 for i in range(5)]
k=1
for i in range(5):
    for j in range(5):
        arr[i][j] = k
        k += 1

# arr = [list(map(int, input().split())) for i in range(5)]
# 모든 칸의 이웃을 출력
for i in range(5):
    for j in range(5):
        if j+1 <= 4:
            print(arr[i][j+1], end=' ')
        if i+1 <= 4:
            print(arr[i+1][j], end=' ')
        if j - 1 >= 0:
            print(arr[i][j-1], end=' ')
        if i - 1 >= 0:
            print(arr[i-1][j], end =' ')
        print()
print()

# 모든 칸의 이웃 중 짝수만 출력
for i in range(5):
    for j in range(5):
        # and로 조건 줄때 앞에게 false면 뒤에 조건은 고려안하고 넘아간다
        # 그러므로 이 경우 인덱스 먼저 검사해서 뒤에 조건까지 고려할 수 있도록 한다!!!
        if j+1 <= 4 and arr[i][j+1] % 2 == 0:
            print(arr[i][j+1], end=' ')
        if i+1 <= 4 and arr[i+1][j] % 2 == 0:
            print(arr[i+1][j], end=' ')
        if j - 1 >= 0 and arr[i][j-1] % 2 == 0:
            print(arr[i][j-1], end=' ')
        if i - 1 >= 0 and arr[i-1][j] % 2 == 0:
            print(arr[i-1][j], end=' ')
        print()