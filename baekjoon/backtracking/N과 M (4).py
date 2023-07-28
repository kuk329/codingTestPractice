
# 15652 번

n,m = map(int,input().split())

pick = [0]*m # 선택한 수 저장


def go(index,start,n,m):
    if index==m:
        print(' '.join(map(str,pick)))
        return
    
    for i in range(start,n+1):
        pick[index]=i
        go(index+1,i,n,m)


go(0,1,n,m)