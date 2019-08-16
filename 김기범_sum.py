import sys
sys.stdin = open('input.txt', 'r')

def ver(arr):
    ans = 0
    for i in range(len(arr)):
        total = 0
        for j in arr[i]:
            total += j
        if total >= ans:
            ans = total
    return ans
def hor(arr):
    ans = 0
    for i in range(len(arr[0])):
        total = 0
        for j in range(len(arr)):
            total += arr[j][i]
        if total >= ans:
            ans = total
    return ans

def cross(arr):
    ans = 0
    for i in range(len(arr[0])):
        ans += arr[i][i]
    return ans

def cross_r(arr):
    ans = 0
    for i in range(len(arr[0])):
        ans += arr[i][len(arr) - i - 1]
    return ans

T = 10
for i in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    h = hor(arr)
    v = ver(arr)
    c = cross(arr)
    cr = cross_r(arr)
    ans = max(h, v, c, cr)

    print('#{} {}'.format(tc, ans))

    """
    행의 합과 열의 합이 비슷하므로
    합칠수 있다.
    행과 열을 합
    ans = 0
    for i in range(len(arr[0]):
        s1 = 0
        s2 = 0
        for j in range(len(arr)):
            s1 += arr[j][i]
            s2 += arr[i][j]
        if s1 > ans:
            ans = s1
        if s2 > ans:
            ans = s2
            
    대각선도 줄일 수 있음
    
    s3 += arr[i][i]
    s4 += arr[i][len(N)-1-i]
    을 위 for문에 넣어줄 수 있음
    
    그리고 for문 밖에 대소비교 조건문 추가
    
    if s3 > ans:
        ans = s3
    if s4 > ans:
        ans = s4
    """
