from collections import deque

def solution(n_str):
    answer = ''
    q=deque(n_str)
    while q:
        if q[0]=='0':
            q.popleft()
        else:
            break
        
    answer=''.join(q)
    return answer


def solution(n_str):
    return n_str.lstrip('0')



def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i]!="0":
            return n_str[i:]