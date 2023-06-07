# 0/1 knapsack 
# 배낭에 담을수 있는 무게의 최댓값이 정해져 있고, 일정한 가치의 무게가 정해진 짐들을 배낭에 담을때, 가치가 최대가 되는 조합을 찾는 알고리즘.

# 종류
# - Fractional Knapsack : 물건을 쪼개서 담는게 가능하면 greedy 로 풀수 있음.
# - Knapsack : 물건을 쪼개서 담는게 불가능 하면 dp 로 풀수 있음.


n,W = map(int,input().split()) # 아이템 개수, 최대 무게 

arr=[[0,0]]

for _ in range(n):
    arr.append(list(map(int,input().split()))) # 아이템 무게와 가치 저장


dp = [[0]*(W+1) for _ in range(n+1)] # table 

for i in range(1,n+1):
    for j in range(W+1):
        w = arr[i][0] # 무게
        p = arr[i][1] # 가치
        if j<w: # 해당 아이템이 가방에 넣을수 없으면 
            dp[i][j] = dp[i-1][j]
        else: # 가방에 넣을수 있으면
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+p)

print(dp[n][W])










