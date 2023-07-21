# 1764

n,m = map(int,input().split())


not_see = set()
not_hear = set()

for _ in range(n):
    not_see.add(input())

for _ in range(m):
    not_hear.add(input())



not_see_hear = not_see & not_hear

result=sorted(list(not_see_hear))


print(len(result))
for name in result:
    print(name)
