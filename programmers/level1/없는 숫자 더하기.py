

def solution(numbers):
    arr=[i for i in range(0,10)]
    set_num = set(arr)-set(numbers)
    return sum(set_num)
    
    
def solution(numbers):
    answer = 0
    arr=[0]*10
    
    for num in numbers:
        arr[num]=1
        
    for i in range(10):
        if arr[i]==0:
            answer+=i

    
    return answer


def solution(numbers):
    return 45-sum(numbers)


def solution(numbers):
    return lambda x: sum(range(10))-sum(x)