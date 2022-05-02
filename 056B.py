w,a,b=map(int, input().split())

if (a+w)<b:
    print(b-(a+w))
elif (a+w)>=b>=a or (a+w)>=(b+w)>=a:
    print(0)
else:
    print(a-(b+w))