# num_list : 정수 리스트
# 마지막 원소가 그전 원소보다 크면 마지막 원소 - 그전 원소 : 마지막 원소*2

def solution(num_list):
    tmp=0
    answer = []
    last = num_list[-1] # 마지막 원소
    before_last = num_list[-2] # 마지막 원소 그 이전
    if last>before_last:
        tmp = last - before_last
    else:
        tmp=last*2
        
    num_list.append(tmp)
    return num_list



def solution(arr):
    arr.append(arr[-1]-arr[-2] if arr[-1]>arr[-2] else arr[-1]*2)
    return arr