import sys
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
input = sys.stdin.readline
mylist=[]
n,l = map(int, input().split())

for x in range(n):
    mylist.append(input())

mylist=sorted(mylist)
ans=''
for j in range(len(mylist)):
  ans = ans + mylist[j]
print(ans)

#なにやってもlistの出力が改行される対策わからん死んだ）