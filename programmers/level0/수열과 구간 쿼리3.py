# 정수 배열 : arr
# 2차원 정수 배열 queries

def solution(arr, queries):
    answer = []
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]

    return arr

result=solution([0, 1, 2, 3, 4],[[0, 3],[1, 2],[1, 4]])
print(result)