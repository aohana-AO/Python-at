n=input()

t=list(map(int, input().split()))
m=int(input())

ts2=[]


for i in range(m):
    p,x=map(int, input().split())
    ts2.append(int(sum(t))-t[p-1]+x)    

for i in ts2:
    print(i)

    
    


