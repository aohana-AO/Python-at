import re
n,m=map(int, input().split())
a,b=[],[]
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
end=0
j=0
moji='x'

for i in range(n):
        
        if b[j] in a[i]:
          
            if j==0 or moji==a[i].find(b[j]):
                if j==m-1:
                    end=1
                    print("Yes")
                    break
                moji=a[i].find(b[j])
                b[j]=b[j][moji:]
                j+=1
                
                
            else:
                if moji==a[i-1].find(b[j-1]):
                    moji=a[i].find(b[j])
                    i-=1
                    

                j=0
                moji='x'
        else:
            j=0
            moji='x'

if end==0:
    print("No")

    #じかんかかりすぎわけわからんなったからあきらめる




