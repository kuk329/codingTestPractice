from collections import deque

n,k = map(int,input().split())
visited=[-1]*100001

def bfs(n):
    q = deque()
    q.append(n)
    visited[n]= 0 # 시작점은 0초
    while q:
        x = q.popleft() 
        if x==k:
            break

        if x-1>=0 and visited[x-1]==-1:
            visited[x-1]=visited[x]+1
            q.append(x-1)
        if x+1<100001 and visited[x+1]==-1:
            visited[x+1]=visited[x]+1
            q.append(x+1)
        if x*2<100001 and visited[x*2]==-1:
            visited[x*2]=visited[x]
            q.append(x*2)

             
bfs(n)
print(visited[k])