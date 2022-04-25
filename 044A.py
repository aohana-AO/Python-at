import sys
input = sys.stdin.readline

n=int(input())
k=int(input())
x=int(input())
y=int(input())
if(n<=k):
    print(n*x)
else:
    print(((n-k)*y+k*x))

#これでいけた、よくわからんもう）
