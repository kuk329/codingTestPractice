
# ======= sol 1 =========
def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if ex in s:
            s=s.replace(ex,"")
            continue
        answer+=s
    return answer




# ======= sol 2 =========

def solution(str_list,ex):
    filter= [s for s in str_list if ex not in s]
    return "".join(filter)