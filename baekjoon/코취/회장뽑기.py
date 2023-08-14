

# a - b 친구
# a - c - b 친구 
# 회장은 점수가 가장 적은 사람 

from collections import deque


n = int(input()) # 회원 수 입력

info=[[] for i in range(n+1)] 



while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    info[a].append(b)
    info[b].append(a)





def bfs(start,visited):
    visited[start]=0   
    q = deque()
    q.append(start)

    while q:
        x=q.popleft()

        for v in info[x]:
            if visited[v]==-1: # 아직 방문을 안했으면
                visited[v]=visited[x]+1
                q.append(v)


    return max(visited)


ans = [[] for i in range(n+1)]
min_value = 100
for i in range(1,n+1):
    visited=[-1]*(n+1) # 이미 친구관계인걸 확인 했는지 여부 + 친구 관계의 거리
    tmp=bfs(i,visited) # i 번의 점수
    ans[tmp].append(i)
    if tmp<min_value:
        min_value=tmp





print(min_value,len(ans[min_value]))
for i in ans[min_value]:
    print(i,end=' ')

