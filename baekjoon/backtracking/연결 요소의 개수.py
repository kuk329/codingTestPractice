# 11724 번
import sys
sys.setrecursionlimit(10**6)

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
