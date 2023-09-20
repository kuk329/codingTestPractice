# 14226 번

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 3. 화면에 있는 이모티콘중 하나 삭제


from collections import deque

n = int(input()) 
dist=[[-1]*(n+1) for _ in range(n+1)]
q=deque()
q.append((1,0))
dist[1][0] = 0 # 화면에 이모티콘 1개 [화면][클립보드]


# ---- sol 1 -----

# while q:
#     s,c = q.popleft()
#     for x,y in [(s,s),(s+c,c),(s-1,c)]:
#         #print(x,y)
#         if 0<=x<=n and 0<=y:
#             if dist[x][y]==-1: # 아직 방문 x
#                 q.append((x,y))
#                 dist[x][y]=dist[s][c]+1


# ans=10000
# for k in dist[n]:
#     if k>=0 and k<ans:
#         ans=k

# print(ans)

    

# ---- sol 2 -----

while q:
    s,c = q.popleft()
    if dist[s][s]==-1: # 화면 -> 클립보드 복사
        dist[s][s]=dist[s][c]+1
        q.append((s,s))
    if s+c<=n and dist[s+c][c]==-1:
        dist[s+c][c]=dist[s][c]+1
        q.append((s+c,c))
    if s-1>=0 and dist[s-1][c]==-1:
        dist[s-1][c]=dist[s][c]+1
        q.append((s-1,c))
    
ans = -1
for i in range(n+1):
    if dist[n][i]!=-1:
        if ans==-1 or ans>dist[n][i]:
            ans=dist[n][i]

print(ans)
