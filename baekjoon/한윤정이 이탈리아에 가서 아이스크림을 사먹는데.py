
n,m = map(int,input().split())

bad=[]
for _ in range(m):
    a,b = map(int,input().split())
    bad.append((a,b))

cnt=0
chk1=False
chk2=False
# 아이스크림 3가지 선택
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            chk1=False
            chk2=False
            for a,b in bad:
                if a in (i,j,k) and b in (i,j,k):
                    chk1=True
                    chk2=True
                    break
            if not chk1 and not chk2:
                cnt+=1
            


print(cnt)