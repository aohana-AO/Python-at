s=input()
a=0
z=0
l=(len(s))
for i in range(l):

    if s[i]=="A":
        a=i
        break
for i in reversed(range(l)):

    if s[i]=="Z":
        z=i
        break


print(z-a+1)


