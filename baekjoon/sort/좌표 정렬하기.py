# 11650

n = int(input())
coordinate =[]
for _ in range(n):
    x,y = map(int,input().split())
    coordinate.append((x,y))



coordinate.sort(key=lambda x:(x[0],x[1]))

for x,y in coordinate:
    print(x,y)