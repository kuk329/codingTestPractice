
# arr='abdfe'
# print(arr)

# new=arr.replace('a','p')
# print(new)



# str="answer"

# print(len(str))


# s="가나다라 마바사"
# ans = s.endswith("마바사")
# print(ans) # True
# ans = s.endswith("마바")
# print(ans) # False


# my_string = "Progra21Sremm3"

# ans=my_string[6:13]
# _ans=ans[::-1] # 문자열 거꾸로 뒤집기

# result = my_string[:6]+_ans+my_string[13:]


# print(result)


# my_string = "ihrhbakrfpndopljhygc"
# c=2
# m=4
# ans=my_string[c-1::m]

# print(ans)

# t="02"
# t=int(t)
# print(t)

# d={}
# alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# print(len(alpha))
# for idx,s in enumerate(alpha):
#     d[s]=0

# print(d)
# answer=list(d.values())
# print(answer)


# import string

# count = dict.fromkeys(string.ascii_uppercase+string.ascii_lowercase,0)

# print(count)


# print(string.ascii_uppercase) #
# print(string.ascii_lowercase) #

# for i in range(10,2,-1):
#     print(i)

# score=[1, 2, 3, 1, 2, 3, 1]
# score.sort(reverse=True) # 내림차순
# print(score)

# data=[]
# n=155
# for i in range(1,n//2+1):
#     if n%i==0:
#         data.append(i)

# data.append(n)

# print(data)


# arr1=[]
# arr2=[1,2,3]
# arr1=arr2
# print(arr1)
# arr2[2]=100
# print(arr1)
# print(arr1==arr2)

# listA = ["A","B","c"]
# listB=listA
# print(listB)
# listA[1]="K"
# print(listB) 

# s1="hello world"
# s2=""
# s2=s1
# print(s2)
# s2[2]="00"
# print(s2)
# print(s1)


# listA = ["A","B","c"]
# listB = listA.copy() # 방법 1
# listC = listA[:]  # 방법 2

# listA.append("D")
# print(listA)
# print(listB)
# print(listC)

# print(listA==listB)


# a=[1,2,3]
# #b=[1,2,3]
# b=a.copy()
# print(a==b)



# s = ["aya", "yee", "u", "maa"]

# s[1]=s[1].replace("ye","hi")
# print(s)


# s="helloworldhello"
# s=s.replace("hello","hi",1)
# print(s)


# from collections import deque

# s="hello world!"
# q=deque(s)
# print(q)



# s=[1,2,3,4]
# print(s[0:8])
# print(s[-2:])



a=str(118372)

for i in a:
    print(i)