def shuffle(cards, card_u, card_d, N):
    X = list(range(N))
    global cnt
    if cards != card_u and cards != card_d:
        if cnt > 5:
            return -1
        else:
            cnt += 1
            for x in X:
                if x > N // 2:
                    x = x - N // 2
                for change in range(N // 2 - 1 - x, N // 2 + x, 2):
                    cards[change], cards[change + 1] = cards[change + 1], cards[change]
                return shuffle(cards, card_u, card_d, N)
    else:
        return cnt

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    cards = list(map(int, input().split()))
    card_u = sorted(cards)
    card_d = card_u[::-1]
    ans = shuffle(cards, card_u, card_d, N)
    print('#{} {}'.format(tc, ans))


