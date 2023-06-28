
# 과일 장수가 사과 상자를 포장준. 사과는 상태에 따라 1점부터 k 점까지 분류
# k 점이 최상품. 1점이 최하품
# 사과 한상자의 가격은 : 사과를 m개씩 담아서 포장. 상자에 담긴 사과중 가장 낮은 점수 : p . 이때 한 상자 가격은 p*m 
# 가능한 많이 팔았을때 최대 이익을 계산. 
# 사과는 상자 단위로만 판매하며, 남은 사과는 버린다.

# 한 상자에 큰수가 있어도 작은수가 있으면 그 수를 곱하기 때문에 무조건 가장 큰수들로만 다 채울수 있으면 채우는걸로,
# 내림차순 정렬해서 가장 큰수부터 담는걸로 그래야 거기 담기는 가장 작은수도 그나마 큰수

def solution(k, m, score):
    answer = 0
    box=[]
    count=0
    score.sort(reverse=True) # 내림차순
    for n in score:
        if count<m:
            box.append(n)
            count+=1
        if count==m:        
            count=0
            answer+=box[-1]*m
            box=[]
    
    
    return answer



print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))