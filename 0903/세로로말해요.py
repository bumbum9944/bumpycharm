import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    maxV = 0
    for word in words:
        if len(word) > maxV:
            maxV = len(word)
    print('#{}'.format(tc), end=' ')
    for c in range(maxV):
        for r in range(5):
            if c < len(words[r]):
                print(words[r][c], end='')
    print()