    # 딕셔너리 두개를 만들어서 x,y에 들어있는 숫자를 세서 저장하고
    # 두개의 딕셔너리를 비교해서 둘중 작은 값을 가져와서 그 숫자들을
    # 배열에 따로 저장해서 내림차순 정렬을 한뒤 그걸로 정수를 만들어서 다시 문자열로
    # 변환해서 반환


def solution(X, Y):
    answer = ""

    d1 = dict()
    d2 = dict()
    arr=[0]*10
    for i in range(0,10):
        d1[i]=0
        d2[i]=0
        
    for x in X:
        d1[int(x)]+=1
        
    for y in Y:
        d2[int(y)]+=1

    # print(f"arr : {arr}")
    # print(f"d1 : {d1}")
    # print(f"d2 : {d2}")
        
    for j in range(0,10):
        tmp = min(d1[j],d2[j])
        # print(f"tmp:{tmp}")
        if tmp!=0: # 두개의 최소값이 0이 아니면 arr 해당 index에 저장
            arr[j]=tmp
    
    # print(f"arr : {arr}")
    # # [2,4,1,1,5,0,3]
    for k in range(9,-1,-1):
        #answer+=str(arr[k])*k
       
        if arr[k]>0:
            answer+=str(k)*arr[k]
            # answer=int(answer)
            # answer=str(answer)

    if len(answer) == answer.count("0"):
        answer="0"
   # print(arr)
        
        
    if sum(arr)==0:
        answer="-1"

    return answer



# ----- other solution ------

# def solution(X, Y):
#     answer = ''

#     for i in range(9,-1,-1) :
#         answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    
#     print(answer)

#     if answer == '' :
#         return '-1'
#     elif len(answer) == answer.count('0'):
#         return '0'
#     else :
#         return answer


print(solution("12321",	"42531"))
print(solution("5525",	"1255"))
print(solution("100","203045"))


