# def solution(n):
    
#     if n==1:
#         return '수'
#     else:
#         if n%2==0:
#             return "수박"*(n//2)
#         else:
#             return "수박"*((n-1)//2)+"수"



def solution(n):

    return "수박"*(n//2) if n%2==0 else "수박"*(n//2)+"수"


print(solution(1))


def solution(n):
    return "수박"*(n//2)+"수"*(n%2)