# 11052 번

n = int(input()) # 구매하려는 카드 갯수
p=[0]
d=[0]*(n+1) # d[i] : 카드 i 개를 구매하는 최대 비용

p+=list(map(int,input().split()))


for i in range(1,n+1):
    for j in range(1,i+1):
        d[i] = max(d[i],d[i-j]+p[j])


    
print(d[n])




