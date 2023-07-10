
n=int(input())

count=0
if n//5>0: # 5로 나누어 떨어지면
    count+=n//5 # 몫을 더함
    n=n%5

if n//2>0:
    count+=n//2
    n=n//2

if n!=0:
    print(-1)
else:
    print(count)





    