import itertools

S, K = input().split()
K = int(K)

l = list(S)

A = []

candidate = set(itertools.permutations(l, len(S)))
candidate = list(candidate)

for i in range(len(candidate)):
    A.append(''.join(candidate[i]))

A.sort()

print(A[K-1])
