arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 가로의 합
for hor in range(len(arr)):
    total = 0
    for i in range(len(arr[hor])):
        total += arr[hor][i]
    print(total)

# 세로의 합
for ver in range(len(arr[0])):
    total_2 = 0
    for j in range(len(arr)):
        total_2 += arr[j][ver]
    print(total_2)