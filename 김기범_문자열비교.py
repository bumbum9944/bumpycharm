T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    ans = 0
    for i in range(len(M)-len(N)+1):
        for j in range(len(N)):
            if M[i+j] != N[j]:
                j += 1
                break
        if j == len(N)-1:
            ans = 1
            break
    print('#{} {}'.format(tc, ans))