def solution(seoul):
    i=0
    for idx,s in enumerate(seoul):
        if s=='Kim':
            i=idx
            break
            
    return '김서방은 %s에 있다'%i