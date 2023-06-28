# 모험가 N 명
# 모험가를 대상으로 공포도 측정
# 공포도가 x 인 모험가는 반드시 x 명 이상으로 구성한 모험가 그룹에 참가해야됨.
# 최대 몇개의 모험가 그룹을 만들수 있는지.

n = int(input()) # 모험가 수를 받음.
arr = list(map(int,input().split()))

arr.sort() # 오름 차순 정렬
count = 0 # 현재까지 그룹에 포함된 사람 수 
group = 0



fear = arr[0]
for i in range(n):
    if arr[i]<=fear:
        count+=1
    if count==fear:
        group+=1
        fear=arr[i+1]
        count = 0

        
print(f'결과 : {group}')

                                                                                                              
    



    
    


