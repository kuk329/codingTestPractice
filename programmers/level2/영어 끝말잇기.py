
n = int(input())

coordinate = list(map(int,input().split()))

d=dict()
for i in range(n):
    d[coordinate[i]]=i # dict 압축전 값: index // index -> 압축 값으로 변경

_coordinate = sorted(coordinate)
# -10 -9 2 4 4 
#  0  1  2 3 3 -> 앞 뒤값과 중복만 아니면 0부터 하나씩 증가

press=[0]
cnt=0
for i in range(1,n):
    if press[-1]!=_coordinate[i]:
        cnt+=1
        press.append(cnt)
        print(f'press : {press[-1]}')
        print(f'coord: {_coordinate[i]}')
    else:
        press.append(cnt)
  



print(press)
 