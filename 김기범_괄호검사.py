import sys
sys.stdin = open('input.txt', 'r')

def check(target):
    box = []
    for i in target:
        if i == '{' or i == '(':
            box.append(i)
        elif i == '}' or i == ')':
            if len(box) != 0:
                if i == '}' and box[-1] == '{':
                    box.pop()
                elif i == ')' and box[-1] == '(':
                    box.pop()
                else:
                    return 0
            else:
                return 0
    if len(box) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    target = input()

    print('#{} {}'.format(tc, check(target)))
