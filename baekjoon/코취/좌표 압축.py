# 18870

n = int(input())

arr1 = list(map(int,input().split()))

arr2=sorted(arr1)

arr3 = []
d1={}
d2={}
for i in range(len(arr1)):
    d1[i]=arr1[i]


s=0

arr3.append((arr2[0],0))
for i in range(1,len(arr1)):
    if arr2[i]!=arr2[i-1]:
        s+=1
        arr3.append((arr2[i],s))
    else:
        arr3.append((arr2[i],s))



for a,b in arr3:
    d2[a]=b

for i in range(len(arr1)):
    print(d2[d1[i]],end = ' ')



