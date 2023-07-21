n = [int(i) for i in list(input())]

n.sort(reverse=True)

result = ''
for x in n:
    result+=str(x)


print(result)