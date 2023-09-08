from collections import deque

n,m = map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(input())

visited=[[False]*m for _ in range(n)]

move=[(1,0),(0,1),(0,-1),(-1,0)]

def bfs(graph,x,y,visited):
    q=deque()
    q.append((x,y))
    visited[x][y]=True # 해당 지점 방문 처리
    while q:
        a,b = q.popleft()
        for dx,dy in move:
            nx,ny=a+dx,b+dy
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]=='0' and visited[nx][ny]==False:  
                    q.append((nx,ny))
                    visited[nx][ny]=True


def dfs(graph,x,y,visited):
    visited[x][y]=True
    for dx,dy in move:
        nx,ny=x+dx,y+dy
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]=='0' and visited[nx][ny]==False:
                dfs(graph,nx,ny,visited)



cnt = 0
for x in range(n):
    for y in range(m):
        if visited[x][y]==False and graph[x][y]=='0':
            bfs(graph,x,y,visited)
            dfs(graph,x,y,visited)
            cnt+=1


print(cnt)