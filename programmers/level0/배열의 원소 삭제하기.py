def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)):
        if arr[i] in delete_list:
            answer.append(arr[i])
    
 
    for i in answer:
         arr.remove(i)
            
    return arr


#print(solution([293, 1000, 395, 678, 94],[94, 777, 104, 1000, 1, 12]))


def solution(arr,delete_list):
    return [i for i in arr if i not in delete_list]

