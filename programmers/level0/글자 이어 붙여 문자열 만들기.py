# my_string : 문자열
# index_list : 정수 배열


# -------- sol 1 --------------

def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])






# ------ sol 2 ----------
def solution(my_string, index_list):
    answer = ''
    d =dict()
    for idx,s in enumerate(my_string):
        d[idx]=s

    for x in index_list:
        answer+=d[x]

    return answer



my_string="cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
print(solution(my_string,index_list))



