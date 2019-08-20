def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    word = input()
    print('#{} {}'.format(tc, palindrome(word)))