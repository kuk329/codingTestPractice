import sys
input = sys.stdin.readline
INF = int(1e9)

test = int(input()) # 전체 테스트 케이스 수 




for t in range(1,test+1):
# 매 케이스 마다 반복
    
    n,m = map(int,input().split()) # 노드 수와, 간선 수 입력받음
    #start = int(input()) # 시작 노드 입력받음
    graph = [[] for i in range(n+1)] # 간선에 대한 정보를 저장하기 위한 리스트 생성
    answer = [INF]*(n+1)



    visited = [False]*(n+1) # 해당 노드를 방문했는지 여부를 저장하기 위한 배열
    distance = [INF]*(n+1) # 최단 거리 테이블을 모두 무한으로 초기화
    result = [INF]*(n+1) # 자기 자신에게 돌아오는데 걸리는 거리값 저장.

    # 간선 정보 저장
    for _ in range(m):
        a,b,c, = map(int,input().split())
        graph[a].append((b,c))

    def get_smallest_node():
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드의 인덱스 저장
        for i in range(1,n+1): # 모든 노드의 저장된 거리 확인
            if distance[i]<min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start]=0
        visited[start]=True
        for j in graph[start]:
            distance[j[0]]=j[1]

        for i in range(n-1): # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
            now = get_smallest_node()
            visited[now]=True
            for j in graph[now]: # 현재 선택된 노드와 연결된 다른 노드 확인
                cost = distance[now] + j[1]
                if cost<distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 쩗은 경우 거리값 갱신
                    distance[j[0]] = cost


    for start in range(1,n+1):

        dijkstra(start)
        #print(f'{start}에서 출발했을때 각 노드까지의 최단 거리 정보 {distance}')
        for j in range(1,n+1): # 시작노드를 제외한 모든 노드에 대해서 
            if j!=start:
                #print(f'j {j}')
                for i in graph[j]: # 해당 노드에서 시작점으로 가는 간선이 존재하면
                    #print(f'graph : {graph[j]}')
                    if i[0]==start and distance[j]!=INF:
                        #print('result 정보 저장')
                        result[j]=distance[j]+i[1] # result 에는 start 노드에서 시작해서 각 노드를 거쳐 다시 시작 노드로 온 정보가 저장.
            #print(f'{start}에서 출발해서 다시 {start}로 왔을때 각 노드를 거쳐 온 정보 저장 {result}')

        answer[start]=min(result)


        visited = [False]*(n+1) # 해당 노드를 방문했는지 여부를 저장하기 위한 배열
        distance = [INF]*(n+1) # 최단 거리 테이블을 모두 무한으로 초기화
        result = [INF]*(n+1) # 자기 자신에게 돌아오는데 걸리는 거리값 저장.

    min_manito=min(answer)
    print(f'{test} {min_manito}')

    

    








