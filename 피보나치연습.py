#  factorial
# def fact(n):
#     if n < 2:
#         return 1
#     else:
#         return n * fact(n-1)
#
# N = 4
# print(fact(N))

# fibonacci
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

def fibo(n):
    global memo
    if n>=2 and memo[n]==0: # 아직 fibo(n)이 계산되지 않은경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n] # fibo(n)이 계산되어 있으면 리턴


N = 4
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))