N = int(input())
S = list(input())
Q = int(input())
T = [0] * Q
A = [0] * Q
B = [0] * Q

for i in range(Q):
    T[i], A[i], B[i] = map(int, input().split())

'''
k = 0

while k < Q:
    if T[k] == 1:
        S[A[k]-1], S[B[k]-1] = S[B[k]-1], S[A[k]-1]
        k += 1
    elif k+1 < Q and T[k] == 2 and T[k+1] == 2:
        k += 2
    else:
        S[:N], S[N:] = S[N:], S[:N]
        k += 1

print(''.join(S))
'''

d = 0 #ダミー変数

for i in range(Q):
    if T[i] == 2:
        d += 1
    elif T[i] == 1 and d % 2 == 0:
        S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
    else:
        if A[i] > N:
            S[A[i]- N -1], S[B[i]- N -1] = S[B[i] - N -1], S[A[i] - N -1]
        elif A[i] <= N and B[i] > N:
            S[N + A[i]-1], S[B[i] - N -1] = S[B[i] - N -1], S[N + A[i]-1]
        else:
            S[N + A[i]-1], S[N + B[i]-1] = S[N + B[i]-1], S[N + A[i]-1]

if d % 2 == 1:
    S[:N], S[N:] = S[N:], S[:N]

print(''.join(S))