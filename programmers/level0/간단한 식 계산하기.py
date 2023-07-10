def solution(binomial):
    answer = 0
    if "+" in binomial:
        arr=[int(i.strip()) for i in binomial.split("+")]
        answer=arr[0]+arr[1]
        
    elif "-" in binomial:
        arr=[int(i.strip()) for i in binomial.split("-")]
        answer=arr[0]-arr[1]
    
    elif "*" in binomial:
        arr=[int(i.strip()) for i in binomial.split("*")]
        answer=arr[0]*arr[1]
        
    return answer



def solution(binomial):
    result=0
    a,op,b=binomial.split()
    a=int(a)
    b=int(b)

    if op=="+":
        result = a+b

    elif op=="-":
        result=a-b

    elif op=="*":
        result=a*b
    
    return result
