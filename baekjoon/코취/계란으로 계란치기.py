

# # n = int(input()) # 계란의 수
# # info = []
# # for i in range(n):
# #     a,b = map(int,input().split()) # 계란의 내구도와 무게 
# #     info.append((a,b))

# # cnt = 0 # 깨진 계란의 수
# # idx = 0
# # while idx<n:
# #     cur_durability,cur_weight = info[idx][0],info[idx][1] # 들고있는 계란
# #     for j in range(i+1,n):




# # for i in range(n): # 가장 왼쪽 계란부터 들기
# #     cur_durability,cur_weight = info[i][0],info[i][1]

# #     # 칠 계란 고르기 
# #     for j in range(n):
# #         if i!=j :
# #             nxt_durability,nxt_weight = info[j][0],info[j][1]

# #     info[i][0]-=nxt_weight # 내구도 감소 
# #     info[j][0]-=cur_weight # 내구도 감소


# # #    1 # 처음 들은 계란(고정)
# # #    2      3      4       5  .....                      # 그 계란으로 칠 계란
# # #    3         그다음 들은 계란





# # 문제의 핵심
# # 1. 제한이 굉장히 적다.
# # 2. 모든 경우의 수를 돌려보는것 말고는 답이 없다.
# # 3. 백트래킹을 구현해서 가능한 모든 경우의 수를 확인할 줄 아는가?

# n = int(input())

# eggs=[]

# for i in range(n):
#     s,w = map(int,input().split())
#     eggs.append([s,w])


# # 계란의 초기 내구도를 다 저장한후, 내구도가 0 보다 작다면 깨졌다라고 판단하기 위한 배열 생성
# visited=[]
# for egg in eggs:
#     visited.append(egg[0])


# answer = 0



#  # --- 핵심 로직 ----

# def dfs(idx): # 현재 내가 선택할 계란의 위치
#     global answer
#     if idx==n:
#         cnt = 0
#         for i in range(n):
#             if visited[i]<=0:
#                 cnt+=1
#         answer = max(answer,cnt)
#         return
    
#     curr_s,curr_w = eggs[idx][0],eggs[idx][1]
#     # 현재 계란으로 다른 계란을 깨지 못하는 경우도 존재
#     # 이 부분을 체크하기 위해 flag 변수 생성. flag 는 다른 계란을 한번이라도 깬적이 있으면 변경
#     flag = False
#     for i in range(n):
#         next_s,next_w = eggs[i][0],eggs[i][1]
#         # 자기 자신을 깨는 경우 제외
#         if i==idx:
#             continue
#         # 현재 계란과 꺠고싶은 계란 모두 내구도가 0 이상이여야함. 하나라도 0이라면 이미 깨진 계란
#         if visited[i]>0 and visited[idx]>0:
#             visited[i]-=curr_w
#             visited[idx]-=next_w

#             flag = True
#             dfs(idx+1)
#             visited[i]+=curr_w
#             visited[idx]+=next_w
#     if flag==False:
#         dfs(idx+1)




# dfs(0)

# print(answer)

