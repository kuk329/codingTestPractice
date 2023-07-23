
N = 10
visited=[False]*N
stack = []



def dfs(graph,start):
    visited[start] = True # 방문처리
    stack.append(start)

    while len(stack)!=0:
        current = stack.pop()

        for nxt in graph[current]:
            if visited[nxt]==False:
                visited[nxt]==True
                stack.append(nxt)



dfs(graph,1)
