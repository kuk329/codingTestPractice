# 정수 배열 : numLog

def solution(numLog):
    d=dict()
    d[1]="w"
    d[-1]="s"
    d[10]="d"
    d[-10]="a"
    answer=''
    
    for i in range(len(numLog)-1):
        tmp = numLog[i+1]-numLog[i]
        answer+=d[tmp]
        
    return answer


def solution(log):
    res=''
    joystick =dict(zip[1,-1,10,-10],['w','s','d','a'])
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    
    return res