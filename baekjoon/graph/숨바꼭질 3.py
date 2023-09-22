# 13549 번

# 거리가 0,1 두가지 이므로 큐 두개를 사용해서 bfs 방식으로 최단거리를 구할수 있다.

from collections import deque
MAX=200000
check = [False]*MAX
dist = [-1]*MAX
n,m = map(int,input().split())

check[n]=True # 초기화
dist[n]=0 # 초기화

q = deque()
nxt_q = deque()

q.append(n)
while q:
    now = q.popleft()
    if now*2 < MAX and check[now*2]==False:
        q.append(now*2)
        dist[now*2]=dist[now] # 순간이동은 0 초
        check[now*2]=True

    if now-1>=0 and check[now-1]==False:
        nxt_q.append(now-1) # 거리가 0 이 아닌 큐에 
        dist[now-1]=dist[now]+1
        check[now-1]=True

    if now+1 <MAX and check[now+1]==False:
        nxt_q.append(now+1)
        dist[now+1] = dist[now] + 1
        check[now+1] = True

    if not q:
        q = nxt_q
        nxt_q= deque()

print(dist[m])


