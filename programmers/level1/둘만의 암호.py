# 두 문자열 s, skip , 그리고 자연수 index
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿈.




def solution(s, skip, index):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s1=set(alpha)
    s2=set(skip)
    s3=s1-s2
    arr=list(s3)
    arr.sort() # set으로 만들면 위치가 다 바뀌므로 정렬을 다시 해줘야됨.
    d=dict()
    for idx,value in enumerate(arr):
        d[value]=idx
    # d = {'a':0,'b':1}
    n=len(arr)
    print(d)

    for i in range(len(s)):
        tmp=d[s[i]] # 바뀌기 전 문자 위치
        print('바뀌기 전 문자, 위치 : ', s[i],tmp)
        tmp=(tmp+index)%n # 바꿀 문자의 위치
        print('바꿀 문자 위치 : ',tmp)
        change=arr[tmp] # 바꿀 문자
        print('바뀔 문자 : ',change)
        s=s.replace(s[i],change,1) # 문자열은 immutable type 이므로 수정이 불가능해서 원래 문자열을 바꾸는건 불가능. 새 문자열 반환
        print(s)
    

    return s


solution("aukks","wbqd",5)