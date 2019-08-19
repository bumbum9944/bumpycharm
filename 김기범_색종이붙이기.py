def paper(N):
    if N <= 1:
        return 1
    else:
        return paper(N-1) + 2 * paper(N-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, paper(N)))

"""
f(n) = f(n-1) + 2*f(n-2)

f = [1] # N = 0
f.append(1) # N = 1
f.append(3) # N = 2
for i range(3, N+1):
    f.append(f[i-1] + 2*f[i-2])
    
f = [0]*(N+1)
f[0] = 1
f[1] = 1
f[2] = 3
for i in range(3, N+1):
    f[i] = f[i-1] + 2*f[i-2]
    
    
f(n)
    if n == 1 :
        return 1
    elif n == 2:
        return 3
    else
        return f(n-1) + 2*f(n-2)
"""