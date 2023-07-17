
from collections import deque
def solution(rank, attendance):
    answer = 0
    ans=[] # 선발된 학생의 번호 저장.
    tmp=[]
    for idx,r in enumerate(rank):
        tmp.append((idx,r)) # index, 랭킹
    tmp.sort(key=lambda x: x[1])
    q=deque(tmp)
    cnt=0 # 선발된 학생수
    for a,b in tmp:
        if attendance[a]==True:
            cnt+=1
            ans.append(a)
            
        if cnt==3:
            break
        
    answer=ans[0]*10000+ans[1]*100+ans[2]
        
    
    return answer


def solution(rank,attendance):
    arr = sorted([(x,i) for i,x in enumerate(rank) if attendance[i]])
    return arr[0][1]*10000 + arr[1][1]*100 + arr[2][1]