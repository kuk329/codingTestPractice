

n,m=map(int,input().split())

arr=list(map(int,input().split()))

map=[[0]*m for _ in range(n)] # 칸에 금광의 정보를 저장하는 배열

d=[0]*m  # 금의 양 누적 

k=0
for i in range(n):
    for j in range(m):
        map[i][j]=arr[k]
        k+=1

max_num=0
for x in range(n):
    max_num=max(max_num,map[x][0])

d[0] = max_num # 초기값 초기화 (첫번째 열에 가장 최대 금)

x=0
tmp=0
for i in range(1,m):
    if x+1>=0 and x+1<m:
        d[i]= map[x,i]+map[x+1][i-1]
    
    if x>=0 and x<m:
        tmp = map[x,i]+map[x][i-1]
        if d[i]<tmp:
            d[i]=tmp
    
    if x-1>=0 and x-1<m:
        tmp = map[x,i]+map[x-1][i-1]
        if d[i]<tmp:
            d[i]=tmp
    

for i in range(1,m):
    for j in range(1,n+1):
        
