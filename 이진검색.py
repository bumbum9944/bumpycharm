"""
개수 N
left = 0
right = N - 1
while left <= right:
# 탐색 구간에 1개의 원소가 남을 때까지
    center = (left + right) // 2
    if key == arr[center]:
        return 1
    else if arr[center] < key:
    # 작은 구간은 버림
        left = center + 1
    else if arr[center] > key
    # 큰 구간은 버림
        right = center - 1
# left > right, 1개 나믄 구간에서도 못 찾으면
return -1

"""