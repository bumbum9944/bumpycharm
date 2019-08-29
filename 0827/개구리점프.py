T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stone = list(map(int, input().split()))
    K = int(input())
    # 개구리의 처음 위치에서 점프
    start = 0
    end = 0
    cnt = 0
    #개구리가 마지막 돌에 착지하면 끝남
    while start != stone[-1]:
        if stone[end+1] - stone[end] > K:
            cnt = -1
            break
        else:
    #점프할 수 있는 거리 안에 돌이 있어야함
            if stone[end+1] - start < K:
                end += 1
                cnt += 1
    #현재 위치 기준 첫번째 돌부터 점프 가능한지 체크
    #점프가 점프가 불가능하면 마지막 점프 가능 돌로 기준위치 이동
            elif stone[end+1] - start > K:
                start = stone[end]
    #점프거리 안에 어떠한 돌도 없으면 -1 출력
    print('Case #{}'.format(tc))
    print(cnt)