n=int(input())
s=input()
c=0
c2=0
for i in range(n):
    if s[i]=="D":
        c-=1
    elif s[i]=="I":
        c+=1
        if c>=c2:
            c2=c

else:
    print(c2)


