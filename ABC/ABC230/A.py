N = int(input())

if N >= 42:
    print("AGC0{}".format(N+1))
elif 10 <= N <= 41:
    print("AGC0{}".format(N))
else:
    print("AGC00{}".format(N))