sa = list(input())
sb = list(input())
sc = list(input())
ssum = [sa,sb,sc]
s = 'a'
z = 0
while z == 0:
  if s == 'a':
    if len(ssum[0]) == 0:
      print('A')
      exit()
    s = ssum[0][0]
    del ssum[0][0]
  elif s== 'b':
    if len(ssum[1]) == 0:
      print('B')
      exit()
    s = ssum[1][0]
    del ssum[1][0]
  elif s == 'c':
    if len(ssum[2]) == 0:
      print('C')
      exit()
    s = ssum[2][0]
    del ssum[2][0]