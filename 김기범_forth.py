def forth(f):
    box = []
    cal = ['+', '-', '*', '/', '.']
    for i in range(len(f)):
        if f[i] == '.':
            if len(box) != 1:
                return 'error'
            else:
                return box[0]
        elif f[i] not in cal:
            box.append(int(f[i]))
        else:
            if len(box) < 2:
                return 'error'
            else:
                if f[i] == '+':
                    a = box.pop()
                    b = box.pop()
                    box.append(b+a)
                elif f[i] == '-':
                    a = box.pop()
                    b = box.pop()
                    box.append(b-a)
                elif f[i] == '*':
                    a = box.pop()
                    b = box.pop()
                    box.append(b*a)
                else:
                    a = box.pop()
                    b = box.pop()
                    box.append(b//a)


T = int(input())
for tc in range(1, T+1):
    f = input().split()
    ans = forth(f)
    print('#{} {}'.format(tc, ans))