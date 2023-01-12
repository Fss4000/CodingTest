'''
DFS와 BFS
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	192977	70339	41658	35.526%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력 1 
1 2 4 3
1 2 3 4

예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1

예제 출력 2 
3 1 2 5 4
3 1 4 2 5

예제 입력 3 
1000 1 100
999 1000

예제 출력 3 
1000 999
1000 999
'''

#입력 노드수 간선수 시작노드
#배열에 노드별 인접한노드 넣기
#큐로 DFS방식인 하나씩 끝까지 호출하여 non Visited 노드 answer 배열에 append
#큐로 BFS호출하여 non Visited 노드 answer 배열에 append

from collections import deque
import queue
import sys
input = sys.stdin.readline
edges=[]
n, m, v = map(int, input().split())
edges=[[] for _ in range(n+1)]
def dfs(edges, e, s):
    answer= []
    visited=[]
    q=deque()
    q.append(s)
    while q:
        now=q.pop()
        if now not in visited:
            visited.append(now)
            print(now, end=' ')
            for i in range(len(edges[now])-1,-1,-1):
                if edges[now][i] not in visited:
                    q.append(edges[now][i])
                    #print('edges[',now,']',edges[now][i],q)
    #print(visited)
    #print('dfs end')
    print()
    return visited

def bfs(edges, e, s):
    answer= []
    visited=[]
    q=deque()
    q.append(s)
    while q:
        now=q.popleft()
        visited.append(now)
        print(now, end=' ')
        for i in range(len(edges[now])):
            if edges[now][i] not in visited and edges[now][i] not in q:
                q.append(edges[now][i])
                #print('edges[',now,']',edges[now][i],q)
    #print('bfs end')
    print()
    return visited



for i in range(m):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1) 
print(edges)

for i in range(1, n+1):
    edges[i]=sorted(edges[i])
dfs(edges, m, v)
bfs(edges, m, v)


#print(sorted(edges))
#print(edges.sort())