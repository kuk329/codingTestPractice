import sys
input = sys.stdin.readline
INF = int(1e9)

test = int(input()) 




for t in range(1,test+1):

    
    n,m = map(int,input().split()) 
    
    graph = [[] for i in range(n+1)] 
    answer = [INF]*(n+1)



    visited = [False]*(n+1)
    distance = [INF]*(n+1) 
    result = [INF]*(n+1) 

    # 간선 정보 저장
    for _ in range(m):
        a,b,c, = map(int,input().split())
        graph[a].append((b,c))

    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1,n+1): 
            if distance[i]<min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start]=0
        visited[start]=True
        for j in graph[start]:
            distance[j[0]]=j[1]

        for i in range(n-1):
            now = get_smallest_node()
            visited[now]=True
            for j in graph[now]: 
                cost = distance[now] + j[1]
                if cost<distance[j[0]]: 
                    distance[j[0]] = cost


    for start in range(1,n+1):

        dijkstra(start)
      
        for j in range(1,n+1):
            if j!=start:
                
                for i in graph[j]: # 
                   
                    if i[0]==start and distance[j]!=INF:
                        
                        result[j]=distance[j]+i[1] 
            

        answer[start]=min(result)


        visited = [False]*(n+1) 
        distance = [INF]*(n+1) 
        result = [INF]*(n+1)

    min_manito=min(answer)
    print(f'{test} {min_manito}')

    

    








# 가장 밖에 arraylist 에는 각 노드 그리고 그안에 arraylist 에는 그 노드와 연결된 노드 여러개가 있을수 있으므로 arraylist 로 선언함.
# 즉 이중 arraylist

