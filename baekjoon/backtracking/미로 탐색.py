# 2178번

# 좌표(그래프) 에서 (1,1) -> (n,m) 까지 가는데 최단거리를 구하고 싶은거니까 
# 넓이 우선탐색 (bfs) 이용. 가중치가 다 같으므로 다익스트라등의 다른 알고리즘을 이용하지 않아도 됨.

from collections import deque


n,m= map(int,input().split()) # n : 세로 , m: 가로

# 좌표니까 상,하,좌,우 움직임 저장
dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited=[[-1]*m for _ in range(n)] # 방문 여부와 거리를 저장하는 배열

graph=[[int(x) for x in list(input()) ] for _ in range(n)]


def bfs(x,y):
    count=1
    d=deque()
    d.append((x,y))  
    visited[x][y]=count
    while d:
        a,b=d.popleft()
        for k in range(4):
            nx=a+dx[k]
            ny=b+dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if visited[nx][ny]==-1 and graph[nx][ny]==1:
                    d.append((nx,ny))
                    visited[nx][ny]=visited[a][b]+1






bfs(0,0)

print(visited[n-1][m-1])