

def solution(n):
    answer = 0
    num=n**(1/2)
    if num == int(num):
        answer=(num+1)*(num+1)
    else:
        answer=-1
 
    return answer