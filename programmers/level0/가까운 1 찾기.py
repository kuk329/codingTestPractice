# arr 은 1 또는 0 인 정수배열

def solution(arr, idx):
    answer = -1
    for index,x in enumerate(arr):
        if idx<=index and x==1:
            answer=index
            break
        
    return answer