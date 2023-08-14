def solution(picture, k):
    answer = []
    x_len= len(picture) # 행 길이
    y_len=len(picture[0]) # 열 길이
    
    for i in range(x_len):
        tmp=''
        for j in range(y_len):
            tmp+=picture[i][j]*k
        for _ in range(k):
            answer.append(tmp)
            
    return answer