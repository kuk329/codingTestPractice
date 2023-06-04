# 11724 번

# --- 인접 리스트 ----

import sys
sys.setrecursionlimit(10**4) # - 파이썬에서 재귀호출을 사용할때 써주는게 좋음.
input=sys.stdin.readline
n,m = map(int,input().split())

visited = [False]*(n+1)

edges = [[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

def dfs(s):
    visited[s]=True
    for e in edges[s]:
        if visited[e]==False:
            dfs(e)


count=0

for i in range(1,n+1):
    if visited[i]==False:
        dfs(i)
        count+=1

print(count)


# ------- 인접 행렬 --------
# 간선의 수가 최대 n^2 이하이므로 간선이 많을때는 인접 리스트의 효율성이 떨어짐

import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

adj = [[0]*n for _ in range(n)]

for _ in range(m):
    a,b=map(lambda x:x-1,map(int,input().split())) # - 실제 좌표는 1,1 부터 시작이므로 -1을 뺌
    adj[a][b]=adj[b][a] = 1

ans=0
visited = [False]*n

def dfs(now):
    for nxt in range(n):
        if adj[now][nxt] and not visited[nxt]:
            visited[nxt]=True
            dfs(nxt)

for i in range(n):
    if not visited[i]:
        ans+=1
        visited[i]=True
        dfs(i)


print(ans)
