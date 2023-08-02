# 4796 번

# 총 휴가 기간동안 연속해서 캠핑장이 여는 기간동안 연속으로 사용할수 있는 최대의 기간을 사용하면 된다.
# 위 조건에 따라서만 풀면 되기 때문에 그리디로 볼수 있다.

cnt = 0
ans=0
while True:
    cnt+=1
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0:
        break

    # 총 휴가 일수를 캠핑장 연속 운영수로 나눈뒤 몫에 연속사용 일수 곱한값을 더한다. 
    # 나머지와 연속사용 일수중 더 작은 값을 더해준다. 
    

    use = V//P
    ans = use*L + min(V%P,L)


    # 결과 출력
    print(f"Case {cnt}: {ans}")

