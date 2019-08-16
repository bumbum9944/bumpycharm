import sys
sys.stdin = open('sample_input.txt', 'r')
def palindrome(arr, N, M):
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if arr[i][j+k] != arr[i][M+j-k-1]:
                    break
            if k == M-1:
                return arr[i][j:j+k+1]
            for k in range(M):
                if arr[j+k][i] != arr[M+j-k-1][i]:
                    break
            if k == M-1:
                ans = ''
                for l in range(M):
                    ans += arr[j+l][i]
                return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

    ans = palindrome(arr, N, M)
    print('#{} {}'.format(tc, ans))

