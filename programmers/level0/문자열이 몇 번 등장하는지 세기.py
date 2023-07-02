from collections import deque
def solution(myString, pat):
    answer=0
    q=deque(list(myString))
    tmp=""
    n=len(pat)
    while q:
        s=q.popleft()
        tmp+=s
        if tmp[-n::]==pat:
            answer+=1
        

    return answer