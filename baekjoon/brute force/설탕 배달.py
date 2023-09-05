# 2839번

# 최대한 적은 개수의 봉지 -> 가능한 5kg 봉지 이용. 

# 5kg 을 최대한 가져가야 됨.
# 3kg 를 하나씩 늘려가면서 3,5 만으로 배달이 가능한지 확인.


sugar = int(input()) # 배달할 설탕 무게

cnt=0

while sugar>=0:
    if sugar%5==0:
        cnt+=sugar//5
        break
    sugar-=3
    cnt+=1


if sugar<0: # 조건 주의
    print(-1)
else:
    print(cnt)