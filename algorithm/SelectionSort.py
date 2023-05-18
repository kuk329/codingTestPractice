# 선택 정렬
# 순차탐색을 하면서 가장 작은 값을 찾아서 맨 앞으로 보내가며 정렬을 한다. (오름차순)

def SelectionSort(arr):
    length=len(arr) # 배열 길이
    for i in range(length-1):
        min=arr[i]
        idx=i # 한번 탐색에서 자장 작은 값의 index 값 저장
        for j in range(i+1,length):
            if arr[j]<min:
                min=arr[j]
                idx=j
        arr[i],arr[idx]=arr[idx],arr[i]
    return arr


arr=[7,5,9,0,3,1,6,2,4,8]
print(SelectionSort(arr))



