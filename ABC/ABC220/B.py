K = int(input())
A, B = input().split()

def k_to_ten(x):
    ans = 0
    for i in range(len(x)):
        ans += (K ** i) * int(x[-(i+1)])
    return ans

a = k_to_ten(A)
b = k_to_ten(B)

print(a*b)