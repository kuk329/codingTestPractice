
# 동명이인이 있으므로 set은 X
# hash (dictionary) 이용


def solution(parti,comple):
    hashDict = {}
    sumHash = 0

    for part in parti:
        hashDict[hash(part)] = part
        sumHash+=hash(part)


    for comp in comple:
        sumHash-=hash(comp)


    return hashDict[sumHash]





parti=["leo", "kiki", "eden"]
comple=["eden", "kiki"]
solution(parti,comple)
