
# 0 과 1로 이루어진 정수 배열 arr. 
# stk : arr을 이용해 만드는 새 배열

def solution(arr):
    stk=[]


    i = 0
    while i<len(arr):
        if not stk: # 빈배열이면
            stk.append(arr[i])
           
        else: # 값이 있으면
            if stk[-1]==arr[i]:
                stk.pop() # 마지막 원소 제거 
            else:
                stk.append(arr[i])
        i+=1

    if stk:
        return stk
    else:
        return [-1]


# ----- sol 2 ------

def solution(arr):
    stk=[]
    for i in range(len(arr)):
        if stk and stk[-1]==arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    
    return stk or [-1]