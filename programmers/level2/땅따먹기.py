
def solution(land):
    answer = 0
    n = len(land)
    d=[[0]*4 for _ in range(n)]
    
    for i in range(4): # 초기값 설정
        d[0][i]= land[0][i]
    
    for i in range(1,n):
        for j in range(4):
            d[i][j] = land[i][j]+max(d[i-1][:j]+d[i-1][j+1:])
            
            
    answer = max(d[n-1])
    return answer