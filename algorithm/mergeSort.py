# merge sort - 정렬 알고리즘.
# Merge sort is defined as a sorting algorithm that works by dividing an array into two half
# sort each half, and then merge the sorted halves back together.

# O(nlogn) - sort large arrays relatively quickly.

# def mergeSort(arr):
#     if len(arr)>1: # 1개일때는 정렬할 필요 x
#         mid=len(arr)//2 # 배열의 가운데 index 찾음.
        
#         left=arr[:mid]

#         right= arr[mid:]

#         mergeSort(left)

#         mergeSort(right)

#         i=j=k=0 

#         while i<len(left) and j<len(right):
#             if left[i]<right[i]:
#                 arr[k]=left[i]
#                 i+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
        
#         while i<len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while j<len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1

# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()



# if __name__ == '__main__':
#     arr=[12,11,13,5,6,7]
#     print("정렬전 array : ")
#     printList(arr)
#     mergeSort(arr) # 합병정렬 수행
#     print("정렬후 array : ")
#     printList(arr)


def merge_sort(arr):
    if len(arr)<2:
        return arr
    
    mid = len(arr)//2
    low_arr=merge_sort(arr[:mid])
    high_arr=merge_sort(arr[mid:])

    merged_arr=[] #정렬이 된 값 저장
    l=h=0 # 오른쪽 왼쪽으로 분열된 배열의 각각의 index를 어디까지 비교했는지 저장
    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l]<high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    
    merged_arr+=low_arr[l:]
    merged_arr+=high_arr[h:]
    return merged_arr

arr=[3,10,5,7,22,28,13,11,100,50]
sorted_arr=merge_sort(arr)
print(sorted_arr)



