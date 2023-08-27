# 11053 번

n = int(input()) # 수열의 크기
a = [0]

a+=list(map(int,input().split()))

d=[0]*(n+1)

d[1]=1

for i in range(2,n+1):
    tmp=0
    for j in range(1,i):
        if a[j]<a[i]:
            tmp=max(tmp,d[j])
    d[i]=tmp+1



#print(d)
print(max(d)) # 출력값 주의


