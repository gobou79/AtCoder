N = int(input())
A = list(map(int, input().split()))
ans = []

if N = 1:
    print(A[0])
else:
    for i in range(1, N):
        a = A[:i]
        b = A[i:]
        cnt_f = 0
        cnt_l = 0
        for i in range(len(a)):
            cnt_f = cnt_f | a[i]
        for i in range(len(b)):
            cnt_l = cnt_l | b[i]
        ans.append(cnt_f ^ cnt_l)

    print(min(ans))
