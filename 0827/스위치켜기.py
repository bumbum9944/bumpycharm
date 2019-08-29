N = int(input())
switches = [2] + list(map(int, input().split()))
students = int(input())
for i in range(students):
    gen, pos = map(int, input().split())
    if gen == 1:
        for j in range(1,N+1):
            if j % pos == 0:
                if switches[j] == 1:
                    switches[j] = 0
                else:
                    switches[j] = 1
                # switches = (switches[j]+1) % 2 라고 써도 됨
    else:
        start = pos
        end = pos
        for k in range(N):
            if start-1 >= 1 and end+1 <= N and switches[start - 1] == switches[end + 1]:
                start = start-1
                end = end+1
            else:
                break
        for m in range(start, end+1):
            if switches[m] == 1:
                switches[m] = 0
            else:
                switches[m] = 1
cnt = 0
for n in switches[1:]:
    cnt += 1
    print(n, end=' ')
    if cnt == 20:
        cnt = 0
        print()