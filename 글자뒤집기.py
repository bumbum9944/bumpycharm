s = list(input())

for i in range(len(s)//2):
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
for i in s:
    print('{}'.format(i), end='')
print()
print(''.join(s))