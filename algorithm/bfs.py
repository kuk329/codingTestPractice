n = int(input())
m = int(input())

computer = [[] for i in range(n+1)]
visited = [False]*(n+1) # 1~ n 번 컴퓨터 방문여부 체크
count = 0
for _ in range(m):
    a,b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)


# def dfs(s):
#     visited[s]=True
    
#     for v in computer[s]:
#         if visited[v]==False: # 아직 방문 안했으면
#             global count
#             count+=1
#             dfs(v) # 방문
           
            
# dfs(1)
# print(count)

stack=[]
def dfs(s):
    global count
    while len(stack)!=0:
        nxt=stack.pop()
        if nxt in