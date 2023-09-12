# 2178번

from collections import deque


n,m = map(int,input().split())

a=[]
d=[[0]*m for _ in range(n)]

for _ in range(n):
    tmp=[int(i) for i in list(input())]
    a.append(tmp)

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    d[i][j]=1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if d[nx][ny]==0 and a[nx][ny]==1:
                    d[nx][ny]=d[x][y]+1
                    q.append((nx,ny))



bfs(0,0)

print(d[n-1][m-1])


