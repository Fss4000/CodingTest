import sys
n = int(input())
sys.setrecursionlimit((n+2))

'''
4. 3 번에서 구현한 함수에서 입력값이 큰 경우 Stack Overflow 가 발생합니다. 이 경우 해결할
수 있는 방법을 구하시오. Ex) factorial(1,000,000)

꼬리재귀 방법 - 값을 바로 연산하여 사용

'''


def factorial_tail(n, total=1):
    if n == 1:
        return total
    #print(n)
    return factorial_tail(n-1,n*total)

print(factorial_tail(n))