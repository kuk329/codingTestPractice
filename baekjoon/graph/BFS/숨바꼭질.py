# 1697번
# 가중치가 모두 1이고 최솟값을 구하고 있으므로 BFS 이용

from collections import deque

MAX=100001
n,k = map(int,input().split())

visited=[False]*MAX # 0~100001
distance=[-1]*MAX


def bfs(s):
    q=deque()
    q.append(s)
    visited[s]=True # 방문 처리
    distance[s]=0

    while q:
        now = q.popleft() # 가장 첫번째 값 꺼내서 저장

        if now-1>=0 and visited[now-1]==False: # 범위를 넘지 않고 아직 방문을 안했으면
            q.append(now-1) # 큐에 삽입
            visited[now-1]=True #  방문 처리
            distance[now-1] = distance[now] + 1 # 거리 정보 update

        if now+1 <MAX and visited[now+1]==False:
            q.append(now+1)
            visited[now+1]=True
            distance[now+1] = distance[now] + 1

        if now*2 <MAX and visited[now*2]==False:
            q.append(now*2)
            visited[now*2]=True
            distance[now*2] = distance[now] + 1


bfs(n)

print(distance[k])
            






