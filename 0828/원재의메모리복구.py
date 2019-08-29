T = int(input())
for tc in range(1, T+1):
    mem = list(map(int, input()))
    # 0으로 초기화된 리스트 만들자
    reset = [0]*len(mem)
    # 원래 메모리와 리셋된 메모리의 각 원소를 비교
    cnt = 0
    for i in range(len(mem)):
    # 같으면 넘어감
        if mem[i] == reset[i]:
            continue
    # 다르면 그 원소 포함 이후 원소들을 원래 메모리의 원소로 모두 바꿔주고 카운트 1추가
        else:
            for j in range(i, len(mem)):
                reset[j] = mem[i]
            cnt += 1
    print('#{} {}'.format(tc, cnt))