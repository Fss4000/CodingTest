from collections import deque
import sys
input = sys.stdin.readline
#우하좌상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count=0
#탐색해서 방문한곳 저장
#방문안한곳이면 숫자 증가
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == n-1 and b == n-1:
            print(count)
            return
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] != 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1
t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)
sorted