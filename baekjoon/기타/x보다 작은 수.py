
n,x = map(int,input().split())
arr=list(map(int,input().split()))

for k in arr:
    if k<x:
        print(k,end=' ')