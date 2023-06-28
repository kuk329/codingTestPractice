
n,k = map(int,input().split())

count = 0

while True:
    if n==1:
        break
    if n%k==0:
        n=n//k
    else:
        n-=1
    count+=1


print(f"결과 : {count}")


# ----- sol 2 -----
# n 이 k 의 배수가 되도록 효율적으로 한번에 뺴는 방식
n,k = map(int,input().split())
result = 0

while True:
    # N==K 로 나누어 떨어지는 수가 될때까지 1씩 빼기
    target = (n//k)*k
    result +=(n-target)
    n = target
    # n 이 k 보다 작을때 반복문 탈출
    if n<k:
        break

    result+=1
    n//=k


result +=(n-1)
print(result)