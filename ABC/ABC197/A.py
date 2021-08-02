S = input()
s = list(str(S))
s_1 = s[0]
s.pop(0)
s.append(s_1)
b = ''.join(s)
print(b)