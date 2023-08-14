# 일직선 상에 여러 집들이 존재
# 특정집 하나에만  안테나 설치
# 효율성을 위해 이 안테나가 있는 집으로 부터 다른 모든 집까지 거리의 총합이 최소가 되도록 설치
# 안테나가 설치될수 있는 위치는 정해저 있음. (집이 있는 위치)

n = int(input()) # 집의 개수 

a=list(map(int,input().split())) # 집이 있는 위치 
a.sort() # 오름차순 정렬

s=0
e=len(a)-1


mid = (s+e)//2
dist = 0
for i in range(n):
    dist+=abs(a[i]-a[mid])

ans = a[mid] # 안테나를 설치할 집의 위치
print(f'dist:{dist}')
print(f'ans:{ans}')


idx = mid + 1
tmp_=0

while idx<n: # 오른쪽으로 이동
    for i in range(n):
        tmp_+=abs(a[i]-a[idx])
    
    if tmp_<dist:
        dist=tmp_ # 가장 최솟값 갱신
        ans=a[idx] # 그때의 안테나를 설치한 집 위치 저장.
    else:
        break    
    idx+=1


idx = mid -1
tmp_=0
while idx>=0: # 왼쪽으로 이동
    for i in range(n):
        tmp_+=abs(a[i]-a[idx])
    
    if tmp_<=dist:
        dist=tmp_ # 가장 최솟값 갱신
        ans=a[idx] # 그때의 안테나를 설치한 집 위치 저장.
    else:
        break
    idx-=1


print(ans)







    
        #  0 1 2 3 
