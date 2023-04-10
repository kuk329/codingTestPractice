# binary Search (이진탐색) - given sorted array
# Iterative(반복) 또는 Recursive(재귀) 방법으로 구현할수 있다.


# Iterative implementaion - O(logn)
def binarySearch(arr,left,right,x):
    while left<right:
        mid=(left+right)//2 # mid = left+(right-left)/2 use this when left+right very large number
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[2,3,4,10,40]
x=2

result = binarySearch(arr,0,len(arr)-1,x)
if result==-1:
    print("찾는값 없음")
else:
    print("찾는 값의 index 는",result)