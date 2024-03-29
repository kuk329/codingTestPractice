# QuickSort - divide and conquer

def partition(arr,low,high):
    pivot = arr[high]

    i = low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1


def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)




array = [10,7,8,9,1,5]
quick_sort(array,0,len(array)-1)
print(array)


