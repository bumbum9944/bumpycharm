# def score(i, s):
#     global cnt
#     if i == N:
#         cnt.add(s)
#     else:
#         score(i+1, s)
#         score(i+1, s+problems[i])
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     problems = list(map(int, input().split()))
#     cnt = set()
#     score(0, 0)
#     print('#{} {}'.format(tc, len(cnt)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    problems = list(map(int, input().split()))
    score = [0] * (sum(problems)+1)
    score[0] = 1
    subset = [0]
    for problem in problems:
        for i in range(len(subset)):
            if not score[subset[i]+problem]:
                score[subset[i] + problem] = 1
                subset += [subset[i] + problem]
    print('#{} {}'.format(tc, len(subset)))