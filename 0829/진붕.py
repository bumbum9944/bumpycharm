import sys
sys.stdin = open('input.txt', 'r')
def boong(mans, N, M, K):
    fish = 0
    for i in range(mans[-1]+1):
        if i != 0 and i % M == 0:
            fish += K
        if i == mans[0]:
            if fish == 0:
                return 'Impossible'
            else:
                fish -= 1
                mans.pop(0)
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    mans = sorted(list(map(int, input().split())))
    print('#{} {}'.format(tc, boong(mans, N, M, K)))