sx,sy,tx,ty=map(int, input().split())
 
ans = ''
 
for i in range(ty - sy):
    ans += 'U'
 
for i in range(tx - sx):
    ans += 'R'
 
for i in range(ty - sy):
    ans += 'D'
 
for i in range(tx - sx + 1):
    ans += 'L'
 
for i in range(ty - sy + 1):
    ans += 'U'
 
for i in range(tx - sx + 1):
    ans += 'R'
 
ans += 'DR'
 
for i in range(ty - sy + 1):
    ans += 'D'
 
for i in range(tx - sx + 1):
    ans += 'L'
 
ans += 'U'
 
print(ans)