

def solution(s):
    check=len(s)
    if check==4 or check==6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False


def solution(s):
    return s.isdigit() and len(s) in [4,6]