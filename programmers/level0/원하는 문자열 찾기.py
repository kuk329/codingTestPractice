# myString 을 앞에서부터 탐색.
# 탐색하는 글자가 pat 의 첫글자와 동일하면 pat 크기만큼의 문자열 비교 아니면 탐색 문자를 그 다음으로 



# def solution(myString, pat):
#     answer = 0
#     n1=len(myString)
#     n2=len(pat)
    
#     for i in range(n1):
#         if myString[i].lower()==pat[0].lower(): 
#             if i+n2-1 <= n1-1:
#                 for j in range(1,n2): 
#                     if myString[i+j].lower()!=pat[j].lower():
#                         break
#                 else:
#                     answer=1
#                     return answer
                        
#     return answer
# print(solution("AbCdEfG","aBc"))
# print(solution("aaAA","aaaaa"))



# ------ other solution  -------

def solution(myString,pat):
    return int(pat.lower() in myString.lower())


print(solution("AbCdEfG","aBc"))
print(solution("aaAA","aaaaa"))
