


def solution(k, score):
    answer = []
    high=[]
    check=0
    # k번째까지 자르겠다는 뜻
    for num in score:
        
        if check==k:
            tmp=high[-1]
            if tmp<num:
                high[-1]=num # 교체 
        elif check<k:
            high.append(num)      
            check+=1
            
        high.sort(reverse=True) # 정렬
        answer.append(high[-1])
        print(high)
    return answer


print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
print("=========")
print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))