N, M = map(int, input().split())

if M == 0:
    print(3 ** N)
else:
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]

    l = [3 for i in range(N)]

    for i in range(M):
        if A[i] > B[i]:
            l[B[i]-1] -= 1
        else:
            l[A[i]-1] -= 1

    k = 1

    for i in range(N):
        k *= l[i]

    if k <= 0:
        print(0)
    else:
        print(k)