from collections import deque


def solution(numbers, target):
    answer = 0
    n = len(numbers)-1
    q = deque()
    q.append((numbers[0],0))
    q.append((-numbers[0],0))

    while q:
        add,idx = q.popleft() 
        if idx<n:
            idx+=1
            q.append((add+numbers[idx],idx))
            q.append((add-numbers[idx],idx))
        else:
            if add == target:
                answer+=1


    return answer




num = [1,1,1,1,1]
target = 3
print(solution(num,target))

num=[4, 1, 2, 1]
target = 4
print(solution(num,target))


