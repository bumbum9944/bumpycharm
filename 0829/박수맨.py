T = int(input())
for tc in range(1, T+1):
    mans = [0] + [int(num) for num in input()]
    clap = mans[1]
    ans = 0
    for i in range(2, len(mans)):
        if mans[i] != 0 and i - 1 > clap:
            ans += i - 1 - clap
            clap += i-1 - clap + mans[i]
        elif mans[i] != 0 and i - 1 <= clap:
            clap += mans[i]
    print('#{} {}'.format(tc, ans))