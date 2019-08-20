def f(i, N, K, s):
    global cnt
    global bit
    global cnt2
    # if i == K:
    #     if s == K:
    #         cnt += 1
    cnt2 += 1
    if i == N: # 나머지 원소를 하나라도 추가하면 K보다 커지므로
        cnt += 1
        return
    elif i == N: # 모든 원소를 고려했지만 합이 K가 아닌경우
        return
    elif s > K:
        return
        # s = 0
        # for j in range(N): # 0~N-1은 원 집합의 원소 1~N을 가리킴
        #     if bit[j] == 1: # j+1이 부분집합에 포함된 경우
        #         s += j + 1
        # if s == K:
        #     cnt += 1
    else:
        f(i + 1, N, K, s) # i번이 가리키는 값은 부분집합에 포함되지 않음
        f(i + 1, N, K, s + i+1) # i번이 가리키는 값을 부분집합에 포함

N = 10 # 1부터 N까지가 집합의 원소
K = 10 # 부분집합의 합
cnt = 0
cnt2 = 0
bit = [0] * N
f(0, N, K, 0)
print(cnt2)