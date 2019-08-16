def atoi(s):
    ans = 0
    j = len(s) - 1
    for i in s:
        ans += int(i) * 10 ** j
        j -= 1
    return ans

def atoi2(s):
    n = 0
    for i in range(len(s)):
        n = n * 10
        n = n + int(s[i])
    return n

def atoi3(s):
    n = 0
    for i in range(len(s)):
        n = n * 10
        n = n + ord(s[i]) - ord['0'] # 아스키코드표 글자의 순서를 이용한 것

s = input()

# print(atoi(s))
print(atoi2(s))