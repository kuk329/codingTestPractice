
t = int(input())



for _ in range(t):
    n=int(input()) # 의상수
    dic={} # 사전에 의상 종류별로 저장
    for _ in range(n):
        a,b=input().split()
        
        if b in dic:
            dic[b].append(a)
        else:
            dic[b]=[a] # key: 의상 종류 , value : 의상 이름
    
    cnt = 1
    for i in dic:
        cnt*=(len(dic[i])+1)


    print(cnt-1)

    
