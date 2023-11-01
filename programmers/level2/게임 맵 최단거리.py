from collections import deque


def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
   
    distance = [[-1]*m for _ in range(n)] # 거리 + 방문 여부 저장

    q = deque()
    q.append((0,0)) # 시작점 부터 큐에 삽입
    distance[0][0] = 1 # 예시에 시작점부터 포함함.

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx=x+dx[k] # 세로
            ny=y+dy[k] # 가로
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if maps[nx][ny]==1 and distance[nx][ny]==-1: # 벽이 아니고 한번도 안가본 곳일때
                    distance[nx][ny]= distance[x][y]+1
                    q.append((nx,ny))

    answer = distance[n-1][m-1]
    print(distance)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))




