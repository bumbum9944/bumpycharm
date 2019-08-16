def f(n, v, arr):
    for idx in range(n):
        if arr[idx] == V: # 키 값을 찾으면
            return idx
    return -1


# 개수 N, 키 V
N, V = map(int, input().split())
arr = list(map(int, input().split()))

print(f(N, V, arr))
