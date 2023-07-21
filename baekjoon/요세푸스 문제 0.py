from collections import deque

n,k  = map(int,input().split())

arr = [i for i in range(1,n+1)]
tmp=[]
q = deque(arr)
cnt=0
while q:
    x = q.popleft()
    cnt+=1
    if cnt!=k:
        q.append(x)
    if cnt==k:
        cnt=0
        tmp.append(x)

tmp=[str(i) for i in tmp]
result=''
result+='<'+', '.join(tmp)+'>'
print(result)
