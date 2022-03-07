from itertools import permutations
s = input()
d=s.islower()
while (d==False and len(s)>=200000):
    s = input() 
    d=s.islower()



s_list = list()
for it in permutations(s):
    s_list.append("".join(it))
print(min(s_list))


"""出力
['add', 'dad', 'dda']
"""