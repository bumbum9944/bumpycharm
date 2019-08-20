N = int(input())
nums = list(range(1, N+1))
target = ['3', '6', '9']
for i in nums:
    count = 0
    for j in str(i):
        if j in target:
            count += 1
    if count != 0:
        print('-'*count + ' ', end='')
    else:
        print(str(i)+' ', end='')