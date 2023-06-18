# 알파벳 대소문자로 이루어진 문자열 : my_string
# my_string 에서 'A' 개수, 'B' 개수, .....
# 'a' ,'b' ,,,, 개수

def solution(my_string):
    answer = []
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    d=dict()
    for idx,s in enumerate(alpha):
        d[s]=0
        
    for k in my_string:
        tmp=d[k]
        tmp+=1
        d[k]=tmp
        
    answer=list(d.values())
        
    return answer


ans=solution("Programmers")
print(ans)