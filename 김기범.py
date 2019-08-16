import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    nm = list(map(int, input().split()))
    N = nm[0]
    M = nm[1]
    nums = list(map(int, input().split()))

    totals = []
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += nums[j]
        totals += [total]

    maxIdx = 0
    minIdx = 0
    for i in range(len(totals)):
        if totals[maxIdx] <= totals[i]:
            maxIdx = i
        if totals[minIdx] >= totals[i]:
            minIdx = i
    gap = totals[maxIdx] - totals[minIdx]
    print('#{} {}'.format(tc, gap))