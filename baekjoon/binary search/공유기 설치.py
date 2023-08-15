import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house =[]
for i in range(n):
    house.append(int(input()))

house.sort() # 오름차순 정렬


s=1 # 공유기 최소 거리
e = house[-1]-house[0] # 최대 거리
result = 0 # 공유기 사이에 최대 거리

while s<=e:
    cnt = 1 # 설치한 공유기 개수  
    establish = house[0] # 마지막 설치 위치(집 위치->집에만 설치 가능하니까)
    mid = (s+e)//2 # 공유기 사이의 최소 거리
    for i in range(1,n):
        if house[i]-establish>=mid:
            establish=house[i] # 그 다음 공유기 설치
            cnt+=1 # 설치한 공유 개수 증가
          
    if cnt<c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 작으면
        e=mid-1 # 공유기 사이의 거리를 축소
    elif cnt>c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 크면
        s=mid+1 # 공유기 사이의 거리를 확대
    else:  # 설치한 공유기 개수와 설치해야되는 공유기 개수가 일치하면 
        result = mid 
        s=mid+1 # 가능한 거리의 최대값을 찾기위해 거리를 늘려가면서 계속 반복문 진행 
       


print(result)

# def binary_search(s,e):
#     result = 0 # 공유기 사이에 최대 거리
#     while s<=e:
#         cnt = 1 # 설치한 공유기 개수  
#         establish = house[0] # 마지막 설치 위치(집 위치->집에만 설치 가능하니까)
#         mid = (s+e)//2 # 공유기 사이의 최소 거리
#         for i in range(1,n):
#             if house[i]-establish>=mid:
#                 establish=house[i] # 그 다음 공유기 설치
#                 cnt+=1 # 설치한 공유 개수 증가
        
       
#         if cnt<c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 작으면
#             e=mid-1 # 공유기 사이의 거리를 축소
#         elif cnt>c: # 설치한 공유기 개수가 설치해야 되는 공유기 개수보다 크면
#             s=mid+1 # 공유기 사이의 거리를 확대
#         else:  # 설치한 공유기 개수와 설치해야되는 공유기 개수가 일치하면 
#             result = mid 
#             s=mid+1 # 가능한 거리의 최대값을 찾기위해 거리를 늘려가면서 계속 반복문 진행 
       
#     return result




# if n==2:
#     print(house[1]-house[0])
# else:
#     ans=binary_search(start,end)

#     print(ans)
