T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stops = [0] + list(map(int, input().split())) + [N]
    i = 1
    last = 0
    count = 0
    for stop in range(len(stops)-1):
        if stops[stop+1] - stops[stop] > K:
            count = 0
            print('#{} {}'.format(tc, count))
            break
        elif stops[i] - stops[last] <= K:
            i += 1
        else:
            last = i-1
            i += 1
            count += 1
    else:
        print('#{} {}'.format(tc, count))