# 2193 번

n = int(input()) # 구하려는 수의 자리수 

d =[[0]*2 for i in range(n+1)] # 자리수 1~n

# 초기값 설정
d[1][0]=0
d[1][1]=1

for i in range(2,n+1):
    for j in range(2):
        if j==0:
            d[i][j]=d[i-1][0]+d[i-1][1]
        else:
            d[i][j]=d[i-1][0]


print(d[n][0]+d[n][1])