# 문자열 : my_string , m,c : 정수
# m 은 my_string 길이의 약수로만 주어짐. -> 나누어 떨어진다는 뜻. 


# def solution(my_string, m, c):
#     answer = ''
#     arr=[]
#     n=len(my_string)
#     x = n//m
#     s=0
#     e=m
#     for _ in range(x):
#         tmp = my_string[s:e]
#         arr.append(tmp)
#         s+=m
#         e+=m
#     print(arr)
#     for i in range(len(arr)):
#         answer+=arr[i][c-1]
#     return answer

def solution(my_string,m,c):
    return my_string[c-1::m]

print(solution("ihrhbakrfpndopljhygc",4,2))