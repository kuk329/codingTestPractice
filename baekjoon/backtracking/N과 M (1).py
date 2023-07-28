
# =========== sol 1 ============

# n,m = map(int,input().split())

# num = [i for i in range(1,n+1)]
# visited = [False]*n
# answer = []
# def dfs(cnt):
#     if cnt == m:
#         print(*answer)
#         return
#     for i in range(n):
#         if visited[i]==True:
#             continue
#         visited[i]=True
#         answer.append(num[i])
#         dfs(cnt+1)
#         answer.pop()
#         visited[i]=False

# dfs(0)

#               []
#   [1]        [2]       [3]
# [2],[3]    [1],[3]    [1],[2]

# =========== sol 2 ============


n,m = map(int,input().split()) # n 까지 수 중에서 m개를 선택하는 가지수

arr = [False]*(n+1) # 1번부터 n 까지 수가 존재. 사용 여부 저장.
a = [0]*m # 각 자리에 뭐가 들어갔는지 저장.

def go(index,n,m):
    if index==m:
        # 출력
        print(' '.join(map(str,a)))
        return 
    
    for i in range(1,n+1): # 선택할수 있는 수는 1 ~ n
        if arr[i]==False: # i 를 아직 선택 안했으면
            a[index]=i # index 자리에 i 를 넣고
            arr[i]=True # i는 사용했다고 처리
            go(index+1,n,m) # 그 뒤에 자리 숫자도 찾아줌.
            arr[i]=False  # 다시 원상복귀


            

go(0,n,m)