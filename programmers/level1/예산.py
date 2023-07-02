def solution(d, budget):
    count = 0
    d.sort()
    for i in range(0,len(d)):
        if d[i]>budget:
            break
        budget-=d[i]
        count+=1
    return count