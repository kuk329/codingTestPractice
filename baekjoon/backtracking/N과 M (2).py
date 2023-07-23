n,m = map(int,input().split())

num = [i for i in range(1,n+1)]
visited = [False]*n
answer = []

def dfs(cnt,idx):
    if cnt == m:
        print(*answer)
        return
    for i in range(idx,n):
        if visited[i]==True:
            continue
        visited[i]=True
        answer.append(num[i])
        dfs(cnt+1,i+1)
        answer.pop()
        visited[i]=False

dfs(0,0)
