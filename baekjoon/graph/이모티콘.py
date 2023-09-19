# 14226 번

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 3. 화면에 있는 이모티콘중 하나 삭제


from collections import deque

n = int(input()) 
dist=[[-1]*(n+1) for _ in range(n+1)]
q=deque()
q.append((1,0))
dist[1][0] = 0 # 화면에 이모티콘 1개

while q:
    s,c = q.popleft()
    for x,y in [(s,s),(s+c,c),(s-1,c)]:
        #print(x,y)
        if 0<=x<=n and 0<=y:
            if dist[x][y]==-1: # 아직 방문 x
                q.append((x,y))
                dist[x][y]=dist[s][c]+1


ans=10000
for k in dist[n]:
    if k>=0 and k<ans:
        ans=k

print(ans)

    



