# dfs와 bfs

from collections import deque
n,m,s = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for v in graph:
    v.sort()

    
def dfs(s):
    visited[s]=True
    print(s,end=' ')
    for v in graph[s]:
        if visited[v]==False:
            dfs(v)
    
def bfs(s):  
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        x=q.popleft()
        print(x,end=' ')
        for v in graph[x]:
            if visited[v]==False:
                q.append(v)
                visited[v]=True
                
dfs(s)
visited=[False]*(n+1)
print()
bfs(s)