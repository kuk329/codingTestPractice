

from collections import deque

d=deque()
d.append((3,6))
print(d)

a,b = d.popleft()
print(a)
print(b)