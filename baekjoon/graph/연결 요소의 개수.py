# ==== sol 1 ==== 
# (DFS)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m= map(int,input().split()) # n : 정점 수 , m : 간선 수

graph=[[] for _ in range(n+1)] # 1번 ~ n 번

visited=[False]*(n+1)

cnt = 0 # 연결 요소 갯수


for _ in range(m):
    u,v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(s):
    visited[s]=True
    for v in graph[s]:
        if visited[v]==False:
            DFS(v)



for i in range(1,n+1):
    if visited[i]==False:
        DFS(i)
        cnt+=1
  
print(cnt)



# ==== sol 2 ==== 
# (BFS)

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited=[False]*(n+1)

for _ in range(m):
    u,v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


cnt = 0 # 연결 요소 갯수

def BFS(s):
    visited[s]=True
    q=deque()
    q.append(s)
    while q:
        x= q.popleft()
        print(f'x:{x}')
        for v in graph[x]:
            if not visited[v]:
                q.append(v)
                visited[v]=True


for i in range(1,n+1):
    if not visited[i]:
        BFS(i)
        cnt+=1

print(cnt)
