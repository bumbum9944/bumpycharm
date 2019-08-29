T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    rooms = [0] + list(map(int, input().split()))
    # 모두 꺼져있는 방 만들기
    off = [0]*len(rooms)
    # 각 방을 차례대로 비교
    for i in range(1, N+1):
    # 다르면 조작
        if rooms[i] != off[i]:
            for j in range(i, N+1):
                if j % i == 0:
                    off[j] = (off[j]+1) % 2
            cnt += 1
    print('#{} {}'.format(tc, cnt))