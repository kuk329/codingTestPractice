
# 15651 번

n,m = map(int,input().split())

arr = [False]*(n+1)

a = [0]*m # 선택한 수 저장.

def go(index,n,m):
    if index==m: # m개를 골랐으면 출력
        print(' '.join(map(str,a)))
        return 

    for i in range(1,n+1): # 1 ~ n 중에서 하나 고르기 (중복 허용)
        a[index]=i
        go(index+1,n,m)


go(0,n,m)