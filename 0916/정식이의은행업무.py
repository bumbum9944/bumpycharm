def findfind():
    global bibi, tritri
    bb = [0, 1]
    tt = [0, 1, 2]
    bi_set = []
    for i in range(len(bibi)):
        bibi_copy = bibi[::]
        for b in bb:
            if int(bibi[i]) != b:
                bibi_copy[i] = b
        temp1 = 0
        num = 1
        for r in range(len(bibi_copy)-1, -1, -1):
            if r == len(bibi_copy)-1:
                temp1 += 1 * int(bibi_copy[r])
            else:
                temp1 += int(bibi_copy[r]) * 2**num
                num += 1
        bi_set.append(temp1)
    for i in range(len(tritri)):
        for t in tt:
            tritri_copy = tritri[::]
            if int(tritri[i]) != t:
                tritri_copy[i] = t
                temp2 = 0
                num = 1
                for r in range(len(tritri_copy)-1, -1, -1):
                    if r == len(tritri_copy)-1:
                        temp2 += 1 * int(tritri_copy[r])
                    else:
                        temp2 += int(tritri_copy[r]) * 3**num
                        num += 1
                if temp2 in bi_set:
                    return temp2
T = int(input())
for tc in range(1, T+1):
    bibi = list(input())
    tritri = list(input())
    ans = findfind()
    print('#{} {}'.format(tc, ans))