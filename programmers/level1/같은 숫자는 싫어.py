
from collections import deque
def solution(arr):
    answer = []
    q=deque(arr)
    answer.append(q.popleft())
    while q:
        out=q.popleft()
        if answer[-1]!=out:
            answer.append(out)
    return answer