# 15654번

n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort() # 오름차순 정렬

a=[0]*m # 고른 수열 저장

visited =[False]*n # 고른 숫자 확인

def go(index,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    
    for i in range(n):
        if visited[i]==False:
            num=arr[i]
            visited[i]=True
            a[index]=num
            go(index+1,n,m)
            visited[i]=False

        


go(0,n,m)