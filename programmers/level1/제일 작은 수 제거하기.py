
def solution(arr):
    min_num=min(arr)
    idx=arr.index(min_num)
    arr.pop(idx)
    if arr:
        return arr
    else:
        return [-1]