# 정수 : n, 문자열 : control 
# control 은  "w", "a", "s", "d" 로 이루어짐.
# 

def solution(n, control):

    for s in control:
        if s=="w":
            n+=1
        if s=="s":
            n-=1
        if s=="d":
            n+=10
        if s=="a":
            n-=10

    return n


def solution(n,control):
    key = dict(zip(["w","s","d","a"],[1,-1,10,-10]))
    return n+sum([key[c] for c in control])