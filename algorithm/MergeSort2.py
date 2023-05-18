# mergeSort - divide and conquer
# O(nlogn)

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L = arr[:mid] # divide
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

arr=[9,12,3,4,11,13,5,27,6,7,1]
mergeSort(arr)
print(arr)



