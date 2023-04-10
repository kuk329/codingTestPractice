#알고리즘 수업 - 너비 우선 탐색 1
#너비 우선 탐색이므로 큐 (파이썬에서는 deque) 사용
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,r=map(int,input().split())

visited=[0]*(n+1) # 방문 여부 & 방문 순서 저장
cnt=1 # 방문 순서 count

arr=[[] for _ in range(n+1)] #정점과 간선 정보를 인접 리스트에 저장

for i in range(m): # 간선 정보 저장
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for e in arr: # 간선을 오름차순으로 정렬.
    e.sort() 


def bfs(s):
    global cnt
    q=deque()
    q.append(s)
    visited[s]=cnt
    while q:
        x=q.popleft()
        for v in arr[x]:
            if visited[v]==0: # 정점 방문 여부 확인
                q.append(v)
                cnt+=1
                visited[v]=cnt
                
bfs(1)

for i in range(1,n+1):
    print(visited[i])

