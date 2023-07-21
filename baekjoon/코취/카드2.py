# 2164 번
from collections import deque

n = int(input())

cards = [i for i in range(1,n+1)]

q=deque(cards)


while len(q)>1:
    q.popleft()
    x=q.popleft()
    q.append(x)


print(q[0])