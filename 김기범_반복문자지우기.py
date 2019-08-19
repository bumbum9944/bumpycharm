def solo(word):
    solo_list = []
    for i in word:
        if len(solo_list) == 0:
            solo_list.append(i)
        elif i != solo_list[-1]:
            solo_list.append(i)
        else:
            solo_list.pop()
    return len(solo_list)

T = int(input())
for tc in range(1, T+1):
    word = input()
    print('#{} {}'.format(tc, solo(word)))