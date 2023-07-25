# sol1 - DFS
def solution(n, computers):
    answer = 0
    visited = [False]*n # 방문여부 확인
    for i in range(n): # 하나씩 탐색
        if visited[i]==False:
            DFS(n,computers,i,visited)
            answer+=1           
    return answer

def DFS(n,computers,s,visited):
    visited[s]=True # 방문 처리
    
    for i in range(n):
        if i!=s and computers[i][s]==1 and visited[i]==False:
            DFS(n,computers,i,visited)
            
            

# sol2 - BFS

# from collections import deque

# def solution(n,computers):
#     answer = 0
#     visited= [False]*n
    
#     for i in range(n):
#         if visited[i]==False:
#             print(f'BFS 호출 : {i}')
#             BFS(n,computers,i,visited)
            
#             answer+=1

#     return answer


# def BFS(n,computers,s,visited):
#     q=deque()
#     q.append(s)
#     l=0
#     while q:
#         x = q.popleft()
#         print(f'q while호출 :{x}')
#         visited[x]==True
#         for v in range(n):
#             if v!=x and computers[x][v]==1:
#                 if visited[v]==False:
#                     q.append(v)
#         l+=1
#         if l==10:
#             break


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
