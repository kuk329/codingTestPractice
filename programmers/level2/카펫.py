def solution(brown, yellow):
    answer = [] 
    y_x = 0 # 가로
    y_y = 0 # 세로
    for i in range(1,yellow+1):
        if yellow%i==0: # 노란 타일을 놓을수 있는 모든 방법을 확인
            y_x = i
            y_y = yellow//i
            if y_x*2 + y_y+2 + 4 == brown:
                answer.append(y_x)
                answer.append(y_y)
                
                return sorted(answer,reverse=True)

    
    