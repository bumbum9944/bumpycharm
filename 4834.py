# 숫자 카드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = input()
    card = [0] * 10
    for i in range(0, N):
        v = int(num[i])
        card[v] = card[v] + 1

    maxIdx = 0

    for i in range(0, 10):
        if card[maxIdx] <= card[i]:
            maxIdx = i
    print('#{} {} {}'.format(tc, maxIdx, card[maxIdx]))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = int(input())
    card = [0] * 10
    for i in range(N):
        v = num % 10
        card[v] = card[v] + 1
        num = num // 10

    maxIdx = 0

    for i in range(0, 10):
        if card[maxIdx] <= card[i]:
            maxIdx = i

    print('#{} {} {}'.format(tc, maxIdx, card[maxIdx]))
