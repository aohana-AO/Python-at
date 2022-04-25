import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

x=0

if a==5 or a==7:
    if b==5 or b==7:
        if c==5 or c==7:
            if a+b+c==17:
                x=1
                print('YES')


if x==0:
    print('NO')

#割と数分で行けた
# 	PyPy3 (7.3.0)	100	261 Byte		88 ms	61732 KB
#	Python (3.8.2)	100	261 Byte		23 ms	9164 KB