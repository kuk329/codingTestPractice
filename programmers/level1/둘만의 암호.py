# 두 문자열 s, skip , 그리고 자연수 index
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿈.


# def solution(str,skip,index):
#     answer=''
#     tmp2=0
#     ch=0
#     add=0
#     for s in str:
#         add=0
#         print('s :' ,s)
#         for _ in range(index):
#             add+=1
#             ch=ord(s)+add
#             if chr(ch) in skip:
#                 add+=1
                
#         ch=ord(s)+add
        
#         print('ch ,add :',ch,add)
     

#         if ch >122:
#             ch=ch-123
#             ch=97+ch

#         # 바뀐값 넣어줌.    
#         answer+=chr(ch)
#     print('answer',answer)
#     return answer



# print(solution("klmnopqrstuvwxyz","abcdefghij",20))
# print(solution("aukks","wbqd",5))




def solution(s,skip,index):
    answer=""

    alpha="abcdefghijklmnopqrstuvwxyz" # 알파벳 저장

    for ch in skip: 
        if ch in alpha:
            alpha = alpha.replace(ch,"") # 해당 문자 삭제


    for k in s:
        change = alpha[(alpha.index(k)+index) % len(alpha)]
        answer+=change

    return answer