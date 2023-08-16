# 13305 번

# 무조건 가장 기름값이 작은 도시의 기름으로  -> 그리디

n = int(input()) # 도시의수
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

result = 0
min_price = price[0]
for i in range(n-1):
    if price[i]<min_price:
        min_price=price[i]
    result +=min_price*distance[i]


print(result)