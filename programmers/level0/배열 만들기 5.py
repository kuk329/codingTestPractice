# 문자 배열 : intStrs , 정수 : k,s,l

# def solution(intStrs, k, s, l):
#     answer = []
#     return answer



def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        tmp=''
        tmp=x[s:s+l]
        
        tmp=int(tmp)
        if tmp>k:
            answer.append(tmp)
        
    return answer



intStrs=["0123456789","9876543210","9999999999999"]
k=50000
s=5
l=5
print(solution(intStrs,k,s,l))



