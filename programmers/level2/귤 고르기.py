# 각 귤의 종류별로 몇개씩 있는지 분류후 가장 갯수가 많은 종류부터 담는걸로

def solution(k, tangerine):
    answer = 0
    d= dict() # 귤 종류별로 몇개 있는지 
    for i in range(len(tangerine)):
        if tangerine[i] in d:
            d[tangerine[i]]+=1
        else:
            d[tangerine[i]]=1
            
    #print(d)
    # 귤의 갯수가 많은 귤 종류 먼저 골라서 고르는 귤의 종류가 최소로 만들기
    a = sorted(d.items(),key=lambda x: x[1],reverse=True)
    for x,y in a: # x : 귤 종류 , y : 귤 갯수
        if k<=0:
            break
        k=k-y
        answer+=1
        
    return answer