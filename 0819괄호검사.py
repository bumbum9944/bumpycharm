def f(txt):
    stack = []
    for i in range(len(txt)):
        if txt[i] == '(': # 여는 괄호면 push()
            stack.append(txt[i])
        else: # 닫는 괄호면 pop()해서 비교
            if len(stack) != 0: # 스택이 비어있으면 오류
                stack.pop()
            else:
                return '괄호가 빠졌습니다.'
    #  스택에 여는 괄호가 남아있으면
    if len(stack) != 0:
        return '괄호가 빠졌습니다.'

T = int(input())
for tc in range(1, T+1):
    txt = input()
    print(f(txt))