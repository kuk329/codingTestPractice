# 시간 초과 풀이 

# def solution(players, callings):
#     answer = []
#     # 이름 부른 선수가 위치한 index의 값에 있는 선수와 그 앞에 선수를 맞바꿈.
#     for call in callings:
#         idx=players.index(call)
#         players[idx],players[idx-1]=players[idx-1],players[idx]
#         print(players)
        
#     return players

# players=["mumu", "soe", "poe", "kai", "mine"]
# callings = ["kai", "kai", "mine", "mine"]

# solution(players,callings)

# 통과 풀이 -> hash 함수 (python에서는 dictionary 사용)

def solution(players, callings):
    answer = []
    dic=dict()
    for i in range(len(players)):
        dic[players[i]]=i
        
    for call in callings:
        idx=dic[call]
        before=players[idx-1]
        dic[call]=idx-1
        dic[before]=idx
        players[idx],players[idx-1]=players[idx-1],players[idx]
        
    return players