T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    i = 0
    count = 0
    for stop in stops:
        if i+K == stop:
            i = i+K
            count += 1
        else:
            j = i+K
            while j > stop:
                j -= 1
                if j == i:
                    count = 0
                    break
                else:
                    i = j
                    count += 1
            if count == 0:
                break
    print('#{} {}'.format(tc, count))
