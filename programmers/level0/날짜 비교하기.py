

# ======= sol 1 =========

def solution(date1, date2):
    str1=''
    str2=''
    for i in range(3):
        str1+=str(date1[i])
        str2+=str(date2[i])

        

    return 1 if (int(str1)-int(str2))<0 else 0
  

# ======= sol 2 =========

def solution(date1,date2):
    return int(date1<date2)