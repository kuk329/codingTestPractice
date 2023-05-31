# arr : 정수 배열
# queries : 2차원 정수 배열

def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        tmp = arr[s:e+1]
        max_num = []
        for n in tmp:
            if n>k:
                max_num.append(n)
                
        if len(max_num)>0:
            answer.append(min(max_num))
        else:
            answer.append(-1)
            
                
        
    return answer