# num_list : 정수 리스트



def solution(num_list):
   
    odd=sum(num_list[::2])
    even = sum(num_list[1::2])
    
    return odd if odd>even else even


print(solution([4,2,6,1,7,6]))