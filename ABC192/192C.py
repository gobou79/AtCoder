N, K = map(int, input().split())

def f(x):
    g_2 = int(''.join(sorted(str(x))))
    g_1 = int(''.join(sorted(str(x), reverse = True)))
    return g_1 - g_2



for i in range(K):
    N = f(N)

print(N)
