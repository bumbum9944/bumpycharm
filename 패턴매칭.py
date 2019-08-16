"""
for i : 0 -> N-M # 패턴의 길이 만큼 비교구간을 만들었을 때 시작 인덱스
    for j : 0 -> M-1 #패턴 내부의 비교 위치
        if t[i+j] != p[j]
            break
    if 패턴의 끝까지 비교가 끝나면..
        return 1 # return i (패턴의 시작위치)
return -1 # 패턴이 존재하지 않음
"""