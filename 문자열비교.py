def f(s1, s2):
    i = 0 # 비교할 글자의 인덱스
    while i < len(s1) and i < len(s2): # 어느 문자열의 끝이 아니고
        if s1[i] == s2[i]:
            i = i + 1
        else:
            break
    if i == len(s1) and i == len(s2): # 마지막 글자까지 같고 동시에 종료
        return 1
    else:
        return 0


s1 = input()
s2 = input()

