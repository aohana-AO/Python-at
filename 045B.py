
sa=input()
sb=input()
sc=input()

dore=sa[0]
sa=sa[1:]
gu=True

if len(sa)==0:
        print("A")
        gu=False

while gu:
   
    
    if dore=="a":
        if len(sa)==0:
            print("A")
            break
        dore=sa[0]
        sa=sa[1:]
        
    if dore=="b":
        if len(sb)==0:
            print("B")
            break
        dore=sb[0]
        sb=sb[1:]
        
    if dore=="c":
        if len(sc)==0:
            print("C")
            break
        dore=sc[0]
        sc=sc[1:]
        

