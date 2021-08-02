import math

N = int(input())
A = list(map(int, input().split()))

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


B = A[:math.floor(N/2)]
C = A[math.ceil(N/2):]

C.reverse()

l = []

for i in range(len(B)):
    if B[i] != C[i]:
        if B[i] < C[i]:
            l.append([B[i], C[i]])
        else:
            l.append([C[i], B[i]])

m = get_unique_list(l)

k = len(m)
ans = 0

while k > 1:
    a = m[-1][0]
    b = m[-1][1]
    m.pop()
    for i in range(len(m)):
        if m[i][0] == a:
            m[i][0] = b
        if m[i][1] == a:
            m[i][1] = b
        if m[i][0] > m[i][1]:
            m[i][0], m[i][1] = m[i][1], m[i][0]

    m = get_unique_list(m)

    ans += 1
    k = len(m)

if k == 1:
    ans += 1

print(ans)