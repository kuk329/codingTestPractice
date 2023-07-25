# 19532번

a,b,c,d,e,f= map(int,input().split())

# sol1 -- 완전 탐색 이용

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x+b*y-c)==0 and (d*x+e*y-f)==0:
            print(x,y)
            break


# sol 2 -- 연립방정식 이용

x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)

print(x,y)

