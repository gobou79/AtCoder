n = int(input())
a = [input() for i in range(n)]
b = []
for i in range(n):
    if a[i].startswith('!') == True:
        b.append(a[i][1:])
a_b_ = list(set(a) & set(b))
if len(a_b_)>0:
    print(a_b_[0])
else:
    print('satisfiable')