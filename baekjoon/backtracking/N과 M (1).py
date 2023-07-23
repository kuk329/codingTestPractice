n,m = map(int,input().split())

num = [i for i in range(1,n+1)]
visited = [False]*n
answer = []
def dfs(cnt):
    if cnt == m:
        print(*answer)
        return
    for i in range(n):
        if visited[i]==True:
            continue
        visited[i]=True
        answer.append(num[i])
        dfs(cnt+1)
        answer.pop()
        visited[i]=False

dfs(0)

#               []
#   [1]        [2]       [3]
# [2],[3]    [1],[3]    [1],[2]