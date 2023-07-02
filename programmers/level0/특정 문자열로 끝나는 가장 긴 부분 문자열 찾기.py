
# myString 최대 길이가 20 이므로 시간초과 걱정 Xf
from collections import deque
def solution(myString, pat):
    answer = ''
    tmp=''
    idx=0
    n=len(pat)
    q=deque(list(myString))
    while q:
        s=q.popleft()
        tmp+=s
        if tmp[-n::]==pat:
            idx=len(tmp)-1
            
    # print(tmp)
    new_arr=tmp[:idx+1]
    answer=''.join(new_arr)
    return answer


myString="AbCdEFG"
pat=	"dE"
print(solution(myString,pat))
myString="AAAAaaaa"
pat="a"
print(solution(myString,pat))