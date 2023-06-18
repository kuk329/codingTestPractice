# 정수 n과 k

def solution(n, k):
    answer = []
    tmp = k
    i=1
    while tmp<=n:
        answer.append(tmp)
        i+=1
        tmp=k*i
        
        
    return answer


def solution(n,k):
    return [i for i in range(k,n+1,k)]