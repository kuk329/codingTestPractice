
def solution(park, routes):
    answer = []
    col=len(park)
    row=len(park[0])

    
    for i in range(col):
        for j in range(row):
            if park[i][j]=='S':
                s_x=i
                s_y=j
     
                break

                
    four_cardinal_points = ['E','W','S','N']
    four_coordinates = [(0,1),(0,-1),(1,0),(-1,0)]
    
    result_x=s_x
    result_y = s_y
    
    for step in routes:
        direction,iteration = step.split(' ')
        iteration = int(iteration)
        
        for i in range(4):
            if direction==four_cardinal_points[i]:
                move_x=four_coordinates[i][0]
                move_y=four_coordinates[i][1]
          
                break

        temp_result_x=result_x
        temp_result_y=result_y   

        for i in range(iteration):
            temp_x= temp_result_x + move_x 
            temp_y = temp_result_y + move_y
    
                   
            if temp_x >=0 and temp_x<col and temp_y>=0 and temp_y<row and park[temp_x][temp_y]!='X':
        
                temp_result_x+=move_x
                temp_result_y+= move_y

           
            else:
       
                temp_result_x=result_x
                temp_result_y=result_y
                break

        result_x=temp_result_x
        result_y=temp_result_y
 
   
                
    answer.append(result_x)
    answer.append(result_y)

    return answer

	
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))