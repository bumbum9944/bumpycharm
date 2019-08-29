T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += sum(arr[i+k][j:j+M])
            if s < temp:
                s = temp
    print('#{} {}'.format(tc, s))


"""
(1) 파리채가 x자 모양이라면(크기는 K)
부분배열의 왼쪽 위 모서리 좌표가 i,j일 때,
s = 0
for m in range(K):
    s += fly[i+m][j+m] #오른쪽아래 방향
    s += fly[i+m][j+K-1-m] # 왼쪽 아래 방향
    
# K가 홀수인 경우 가운데 원소가 두 번 더해지므로
if K%2==1:
    s -= fly[i+K//2][j+K//2] #한 개를 빼줌
    
    
(2) 파리채가 ㄱ,ㄴ,ㄷ,ㅁ 모양인 경우

(3) 파리채의 영역이 i+m, j+n 일때 (0 <=m, n<K)
    m짝수, n홀수
    m홀수, n짝수
    나머지는 구멍이 나서 파리가 죽지 않는다.
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    temp += arr[r][c]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))
    # x자 파리채
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += arr[i+k][j+k]
                temp += arr[i+k][j+M-1-k]
            if M % 2 == 1:
                temp -= arr[i+M//2][j+M//2]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))
    # 파리채가 ㄱ, ㄴ, ㄷ, ㅁ일 때
    #(1) ㄱ
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += arr[i][j+k]
                temp += arr[i+k][j+M-1]
            temp -= arr[i][j+M-1]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))
    # (2) ㄴ
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += arr[i+k][j]
                temp += arr[i+M-1][j+k]
            temp -= arr[i+M-1][j]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))
    # (3) ㄷ
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                temp += arr[i][j+k]
                temp += arr[i+k][j]
                temp += arr[i+M-1][j+k]
            temp -= arr[i+M-1][j]
            temp -= arr[i][j]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))
    # (4) ㅁ
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for k in range(M):
                temp += arr[i][j + k]
                temp += arr[i + k][j]
                temp += arr[i + k][j + M - 1]
                temp += arr[i + M - 1][j + k]
            temp -= arr[i + M - 1][j]
            temp -= arr[i][j]
            temp -= arr[i][j+M-1]
            temp -= arr[i+M-1][j+M-1]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))

    # 파리채가 체스판
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    if r % 2 == 0 and c % 2 == 1:
                        temp += arr[r][c]
                    elif r % 2 == 1 and c % 2 == 0:
                        temp += arr[r][c]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    if (r-i) % 2 == 0 and (c-j) % 2 == 1:
                        temp += arr[r][c]
                    elif (r-i) % 2 == 1 and (c-j) % 2 == 0:
                        temp += arr[r][c]
            if temp > s:
                s = temp
    print('#{} {}'.format(tc, s))