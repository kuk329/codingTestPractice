
# ======= sol 1 =========

def solution(num_list, n):
    if n in num_list:
        return 1
    else:
        return 0



# ======= sol 2 =========


def solution(num_list,n):
    return int(n in num_list)