def fibonacci_seq(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    return fibonacci_seq(n-1) + fibonacci_seq(n-2)

print(fibonacci_seq(40))

import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    if num==0:
        memo[num] = 1
        return 1
    if num==1:
        memo[num] = 1
        return 1
    
    memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]
memo={} #global dictionary to store the fibonacci number already computed
# print("Fibonacci number:",fibonacci(40))

'''
Doesn't seem to be faster.
40 without dict: 15.779 seconds
40 with dict: 24.496 seconds
'''
