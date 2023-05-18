# 삽입 정렬 
# 맨 앞에 값은 이미 정렬 되어있다고 가정하고 시작

def InsertionSort(arr):
    length = len(arr)
    for i in range(1,length): # 시작 위치만 알려주는 용도
        for j in range(i,0,-1): #  <--- 왼쪽으로 이동하면서 탐색 
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j] # swap
            else:
                break
    return arr


arr=[7,5,9,0,3,1,6,2,4,8]
print(InsertionSort(arr))








