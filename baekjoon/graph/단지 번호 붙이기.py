# 2667번

dx=[1,-1,0,0]
dy=[0,0,1,-1]
n=int(input())
count=0
apt_count=[]
arr=[[] for _ in range(n)]
visited=[[False]*n for _ in range(n)] 

for i in range(n):
    arr.append(list(input()))


def dfs(i,j):
    global count
    visited[i][j]=True
    count+=1
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if arr[nx][ny]=='1' and visited[nx][ny]==False:
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if arr[i][j]=='1' and visited[i][j]==False:
            count=0
            dfs(i,j)
            apt_count.append(count)


apt_count.sort()
print(len(apt_count))
for x in apt_count:
    print(x)
