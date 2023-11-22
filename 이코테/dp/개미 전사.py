
n = int(input())

dp=[0]*100

foods =list(map(int,input().split()))

dp[0] = foods[0]
dp[1] = max(dp[0],foods[1])

for i in range(2,n):
    dp[i] = max(dp[i-2]+foods[i],dp[i-1])


print(dp[n-1])