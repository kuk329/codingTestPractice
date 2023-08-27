# 16194번 

# --------- sol 1 -----------

n = int(input())
a = [0] + list(map(int,input().split()))
d = [-1]*(n+1)
d[0] = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if d[i] == -1 or d[i] > d[i-j]+a[j]:
            d[i] = d[i-j]+a[j]
print(d[n])


# --------- sol 2 -----------


n = int(input())

p=[0]
p+=list(map(int,input().split()))

d=[1000*10000]*1001

d[0]=0

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i]=min(d[i],d[i-j]+p[j])
        

print(d[n])