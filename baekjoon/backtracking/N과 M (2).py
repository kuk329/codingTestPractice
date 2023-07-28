
# =========== sol 1 ============

# n,m = map(int,input().split())

# num = [i for i in range(1,n+1)]
# visited = [False]*n
# answer = []

# def dfs(cnt,idx):
#     if cnt == m:
#         print(*answer)
#         return
#     for i in range(idx,n):
#         if visited[i]==True:
#             continue
#         visited[i]=True
#         answer.append(num[i])
#         dfs(cnt+1,i+1)
#         answer.pop()
#         visited[i]=False

# dfs(0,0)

# =========== sol 2 ============

# import sys

# n,m = map(int,input().split())
# c = [False]*(n+1)
# a = [0]*m

# def go(index,start,n,m):
#     if index==m:
#         sys.stdout.write(' '.join(map(str,a))+'\n')
#         return
#     for i in range(start,n+1):
#         if c[i]:
#             continue
#         c[i] = True
#         a[index] = i
#         go(index+1,i+1,n,m)
#         c[i]=False


# go(0,1,n,m)


n,m =map(int,input().split())

arr = [False]*(n+1)
a = [0]*m # 선택한 수 저장.

def go(index,start,n,m):
    if index==m:
        print(' '.join(map(str,a)))
        return
    
    for i in range(start,n+1):
        if arr[i]==False:
            arr[i]=True # 선택 처리
            a[index]=i # 선택한 수 저장
            go(index+1,i+1,n,m)
            arr[i]=False




go(0,1,n,m)
