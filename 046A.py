import sys
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
'''
input = sys.stdin.readline

a=int(input())
b=int(input())
c=int(input())



'''

a, b, c = map(int, input().split())
x=3
if a==b or b==c or c==a:
    x=2
    if a==b==c:
        x=1

print(x)