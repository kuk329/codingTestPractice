def solution(num_list):
    answer = []
    num_list.sort() # 오름차순 정렬
    for i in range(5):
        answer.append(num_list[i])
        
    
    return answer


def solution(num_list):
    return sorted(num_list)[:5]