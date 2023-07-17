from collections import deque

def solution(s):
    answer = -1
    #arr=list(s)
    q=deque(s)
    x=q.popleft()
    stk=[x]
    while q:
        if stk:
            if stk[-1]==q[0]:
                stk.pop()
                q.popleft()
            else:
                stk.append(q.popleft())
        else:
            stk.append(q.popleft())
            
        
    if stk:
        return 0
    else:
        return 1
            
