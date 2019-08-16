import sys
sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for i in range(2,N-2):
        if buildings[i-1] < buildings[i] and buildings[i+1] < buildings[i] and buildings[i-2] < buildings[i] and buildings[i+2] < buildings[i]:
            view = buildings[i] - max(buildings[i-20], buildings[i+2], buildings[i-1], buildings[i+1])
            total += view
    print('#{} {}'.format(tc, total))