# arr : 정수 배열 , queries : 2차원 정수 배열


def solution(arr, queries):
    for s,e in queries:
        for i in range(s,e+1):
            arr[i]+=1
            
    return arr