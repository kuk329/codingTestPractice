# binary Search (이진탐색) - given sorted array
# Iterative(반복) 또는 Recursive(재귀) 방법으로 구현할수 있다.


# recursive implementation - O(logn)

def binarySearch(arr,x,low,high):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,x,low,mid-1)
        else:
            return binarySearch(arr,x,mid+1,high)
    else:
        return -1 # 값을 못찾았을때


arr=[2,3,4,10,40,99,102]
x=102 # 찾고싶은 값

result = binarySearch(arr,x,0,len(arr)-1)

if result!=-1:
    print("Element is present at index %d"%result)
else:
    print("Element is not present in array")