# import sys
# sys.stdin = open('sample_input.txt', 'r')

def password():
    global N, M, arr
    ans_ffff = 0
    code_ex = [
        [3, 2, 1, 1], [2, 2, 2, 1],
        [2, 1, 2, 2], [1, 4, 1, 1],
        [1, 1, 3, 2], [1, 2, 3, 1],
        [1, 1, 1, 4], [1, 3, 1, 2],
        [1, 2, 1, 3], [3, 1, 1, 2]
    ]
    for row in range(N):
        for col in range(M-1, -1, -1):
            if arr[row][col] != '0' and visited[row][col] == 0:
                si = row
                sj = col
                code = ''
                for t in range(len(arr[si])):
                    if arr[si][t] != '0':
                        sj2 = t
                        break
                for i in range(sj, sj2-1, -1):
                    visited[si][i] = 1
                    for j in range(4):
                        if int(arr[si][i], 16) & (1 << j):
                            code = '1' + code
                        else:
                            code = '0' + code
                ccc = len(code)
                idx_i = 0
                for i in range(len(code)-1, -1, -1):
                    if code[i] == '1':
                        idx_i = i
                        break
                code = code[:idx_i+1]
                if ccc != len(code):
                    for _ in range(ccc - len(code)):
                        code = '0' + code
                code_code = ''
                for i in range(len(code)-1, -1, -7):
                    if i >= 6:
                        code_code = code[i-6:i+1] + code_code
                cnt_0 = []
                cnt_1 = []
                cnt0 = 0
                cnt1 = 0
                for c in range(len(code_code)):
                    if code_code[c] == '0':
                        if cnt1 == 0:
                            cnt0 += 1
                        else:
                            cnt0 += 1
                            cnt_1.append(cnt1)
                            cnt1 = 0
                    else:
                        if cnt0 == 0:
                            cnt1 += 1
                        else:
                            cnt1 += 1
                            cnt_0.append(cnt0)
                            cnt0 = 0
                cnt_1.append(cnt1)
                code_key = []
                for i in range(len(cnt_1)):
                    code_key.append(cnt_0[i])
                    code_key.append(cnt_1[i])
                nn = min(code_key)
                code_keyf = [num // nn for num in code_key]
                ans = []
                for i in range(0, len(code_keyf), 4):
                    if code_keyf[i:i+4] in code_ex:
                        ans.append(code_ex.index(code_keyf[i:i+4]))
                ans_f = 0
                for i in range(len(ans)):
                    if i % 2 == 0:
                        ans_f += ans[i]*3
                    else:
                        ans_f += ans[i]
                if ans_f % 10 == 0:
                    ans_ffff += sum(ans)
                    break
    return ans_ffff

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrf = [list(input()) for _ in range(N)]
    arr = []
    for a in arrf:
        if a not in arr:
            arr.append(a)
    N = len(arr)
    M = len(arr[0])
    visited = [[0]*M for _ in range(N)]
    ans = password()
    print('#{} {}'.format(tc, ans))