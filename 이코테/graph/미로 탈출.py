from collections import deque

n,m = map(int,input().split())

arr=[]

for i in range(n):
    arr.append(input())

move=[(1,0),(0,1),(-1,0),(0,-1)]

visited=[[0]*m for _ in range(n)] # 방문 여부와 거리 저장.

cnt=0


def bfs(u,v):
    q=deque()
    q.append((u,v)) # 시작점
    visited[u][v]=1
    while q:
        x,y = q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y]
        for dx,dy in move:
            nx,ny=x+dx,y+dy
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if visited[nx][ny]==0 and arr[nx][ny]=='1': # 아직 방문을 안한 곳 & 괴물이 없는곳 
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
print(bfs(0,0))

