import sys
n = int(input())
sys.setrecursionlimit((n+2))#파이썬은 재귀 호출 기본이 1000번으로 세팅

def factorial(n):
    return n*factorial(n-1)

def factorial_nofw(n):
    if n == 1:
        return 1
    return n*factorial_nofw(n-1)

#print(factorial(n))
print(factorial_nofw(n))
