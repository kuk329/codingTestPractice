
# # 문제의 핵심
# # 1. 특정 노드와 거리가 m 이하인 노드들을 찾아야 한다.
# # 2. 모든 노드를 기준으로 다익스트라를 n번 돌려보면 ?
# # 3. 시간복잡도 O(VElogV) 가 소요된다.

# import heapq

# INF = 1e9
# n,m,r = map(int,input().split())
# item=[0]+list(map(int,input().split()))
# graph = [[] for _ in range(n+1)]

# for i in range(r):
#     x,y,z= map(int,input().split())
#     graph[x].append((y,z))
#     graph[y].append((x,z))


# def dijktra(start,visit):
#     pq=[]
#     heapq.heappush(pq,(0,start))
#     visit[start]=0
#     while pq:
#         dist,curr_node = heapq.heappop()







# maxi = 0

# for curr in range(1,n+1):
#     visit = [INF]*(n+1)
#     dijktra(curr,visit)
#     sumOfItem = 0

#     for i in range(1,n+1):
#         if visit[i]<=m:
#             sumOfItem_=item[i]
#     maxi = max(maxi,sumOfItem)

# print(maxi) 