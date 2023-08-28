
# ---------- sol 1 --------------
def solution(citations):
    answer = 0
    sort_=sorted(citations,reverse=True) # 내림차순 정렬 
    print(sort_)
    for num in sort_:
        if num>answer:
            answer+=1
        else:
            break

    return answer





# ---------- sol 2 --------------

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i]>=l-i:
            return l-i
    return 0





solution([3, 0, 6, 1, 5])