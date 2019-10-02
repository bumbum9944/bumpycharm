T = int(input())
for tc in range(1, T+1):
    number = input().split()
    N = int(number[0])
    hex = number[1]

    print('#{}'.format(tc), end=' ')
    for i in range(N):
        if '0' <= hex[i] <= '9':
            digit = ord(hex[i]) - ord('0')
        else:
            digit = ord(hex[i]) - ord('A') + 10
        for j in range(3, -1, -1):
            if digit & (1 << j) == 0:
                print('0', end='')
            else:
                print('1', end='')
    print()