A = float(input())

B = int(A * 10)

if B % 10 <= 2:
    print(int(A),'-', sep='')
elif B % 10 <= 6:
    print(int(A))
else:
    print(int(A), '+', sep='')