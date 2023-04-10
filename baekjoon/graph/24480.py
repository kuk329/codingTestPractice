#알고리즘 수업 - 깊이 우선 탐색 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r= map(int,input().split())

arr=[[0] for _ in range(n)]
visited=[False]*(n+1)
for _ in range(m):
    u,v=map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

# 내림차순 정렬
for i in range(m):
    arr[i].sort(reverse=True)


def dfs(s):
    visited[s]=True
    print(s)
    for v in arr[s]:
        if visited[v]==False:
            dfs(v)


dfs(1)
