# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n = int(input()) # 도시의 개수 
# m = int(input()) # 버스의 개수 


# # 간선을 관리할 인접 리스트 생성
# graph=[[] for i in range(n+1)] # 도시는 1 ~ n 번까지

# for i in range(m):
#     st,en,v = map(int,input().split())
#     graph[st].append((en,v))

# # 거리를 표기할 방문 배열 생성
# # 1e9으로 모든 거리 초기화
# visit=[INF]*(n+1)

# start,end = map(int,input().split())

# def dijkstra(start):
#     heap=[] # 힙 생성
#     # 시작점 방문 거리 0으로 초기화
#     visit[start] = 0
#     # 힙에는 현재까지의 거리, 현재 노드의 번호 삽입
#     heapq.heappush(heap,(0,start))

#     while heap:
#         dist,curr_node = heapq.heappop(heap)
#         # 현재 노드의 방문 값이 dist 보다 작으면 방문을 수행하지 않음.
#         if visit[curr_node]<dist:
#             continue
#         # 현재 노드와 연결된 다른 노드들 까지의 방문 거리 값을 새로 갱신
#         for next_info in graph[curr_node]:
#             cost = dist+next_info[1]
#             next_node = next_info[0]
#             # 만약 cost가 visit[next_node] 보다 크거나 같다면
#             # 이전에 다른 방법으로 방문하는 방법이 더 빠르기 때문에 수행하지 않음.
#             if cost<visit[next_node]:
#                 visit[next_node]=cost
#                 heapq.heappush(heap,(cost,next_node))


# dijkstra(start)
# print(visit[end])