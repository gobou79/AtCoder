N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

mi1 = max(1-A, 1-B)
ma1 = min(N-A, N-B)

x_left_1, x_right_1 = mi1+A, ma1+A
y_left_1, y_right_1 = mi1+B, ma1+B

mi2 = max(1-A, B-N)
ma2 = min(N-A, B-1)

x_left_2, x_right_2 = mi2+A, ma2+A
y_left_2, y_right_2 = B-ma2, B-mi2

for i in range(P, Q+1):
    ans = ['.' for i in range(R, S+1)]
    for j in range(R, S+1):
        k_i = i - A
        k_j_1 = j - B
        k_j_2 = B - j
        if mi1 <= k_i <= ma1 and k_i == k_j_1:
            ans[j-R] = '#'
        elif mi2 <= k_i <= ma2 and k_i == k_j_2:
            ans[j-R] = '#'
    print(''.join(ans))