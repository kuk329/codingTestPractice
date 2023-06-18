# t,p : 문자열

def solution(t, p):
    answer = 0
    n1=len(t)
    n2=len(p)
    s=0
    e=n2
    compare_num = int(p)
    
    while e<=n1:
        tmp=int(t[s:e])
        print('s:',s,'e:',e)
        print('tmp:',tmp)
        if tmp<=compare_num:
            answer+=1
        s+=1
        e+=1
        
    return answer




t="10203"
p="15"

ans=solution(t,p)
print(ans)