
import collections


l=input()

c = collections.Counter(l)

for i in c:
    if c[i]%2==1:
        print("No")
        exit()

print("Yes")