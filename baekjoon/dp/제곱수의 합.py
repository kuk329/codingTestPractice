# 1699 번

n = int(input())

d = [0]*(n+1) # i : 1 ~ n

for i in range(1,n+1):
    d[i] = i # 나올수 있는 가장 최댓값으로 (ex. 3 = 1^2 + 1^2 + 1^2)
    j=1
    while j*j<=i:
        if d[i]>d[i-j*j]+1:
            d[i] = d[i-j*j]+1

        j+=1

print(d[n])