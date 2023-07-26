# 2589 번
from collections import deque

# L : 육지 , W : 바다
n, m = map(int,input().split())
graph = [input() for _ in range(n)]
# arr2 = [list(input()) for _ in range(n)]

# dis = [[-1]*m for _ in range(n)] # 육지 사이의 거리이자 방문 여부를 저장하는 배열


# 이동 방향
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 모든 육지 사이에 최단 거리를 구하고 그중 가장 큰 값이 답.

def bfs(i,j):
    dis = [[-1]*m for _ in range(n)] # 육지 사이의 거리이자 방문 여부를 저장하는 배열
    dis[i][j] = 0
    q= deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if dis[nx][ny]==-1 and graph[nx][ny]=="L": # 아직 방문 X
                    dis[nx][ny]= dis[x][y]+1
                    q.append((nx,ny))

   
    return max(map(max,dis))

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=="L":
            tmp=bfs(i,j)
            if ans<tmp:
                ans = tmp

print(ans)


