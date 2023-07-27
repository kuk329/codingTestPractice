import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dx=[1,-1,0,0,1,-1,1,-1]
dy=[0,0,1,-1,1,-1,-1,1]

ans=[] # 답 저장


def dfs(x,y,visited,w,h,info):
    visited[x][y]=True
   # print('dfs 호출')

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<h and ny>=0 and ny<w:
            if info[nx][ny]==1 and visited[nx][ny]==False:
               # print(f'nx:{nx}, ny:{ny}')
                dfs(nx,ny,visited,w,h,info)


while True:
    w,h= map(int,input().split())
    if w==0 and h==0:
        break
    info = [list(map(int,input().split())) for _ in range(h)]
    visited=[[False]*w for _ in range(h)] # 방문 여부
    cnt=0
    

    for i in range(h):
        for j in range(w):
            if info[i][j]==1 and visited[i][j]==False:
                dfs(i,j,visited,w,h,info)
                cnt+=1

    ans.append(cnt)


#print(f'ans:{ans}')
for n in ans:
    print(n)





