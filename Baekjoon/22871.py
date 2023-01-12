'''
from collections import deque
import sys
input = sys.stdin.readline
n =int(input())
stones = [int(i) for i in input().split()]


print(stones)
def power(s1, s2):
    p=stones.index(s2)-stones.index(s1)*(1+abs(s1-s2))
    print(p)
    return p

q=deque()
#시작과 끝 사이의 갯수만큼 경우의 수 0~n-2
for i in range(0,n-2):
    q.append(i)
    
'''
INF = 999999999
n = int(input())
dp = [0] + [INF] * (n - 1)
print(dp)
    


