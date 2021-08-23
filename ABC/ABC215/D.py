#参考文献(https://kanpurin.hatenablog.com/entry/2021/08/21/232035)

N, M = map(int, input().split())
A = list(map(int, input().split()))

maxA = max(max(A), M)

k = [True] * (maxA+1) #整数iが問題の条件を満たすかどうか
isprime = [True] * (maxA+1) #iが素数かどうか判定する
prime = [] #Aの素因数

for a in A:
    k[a] = False

for i in range(2, maxA+1):
    if isprime[i] == False:
        continue
    for j in range(i*2, maxA+1, i):
        isprime[j] = False
        #もし素数iの倍数（j）にAの要素があったら，その素数iは使えない！
        if k[j] == False:
            k[i] = False
    #使えない素数をprimeに格納する
    if k[i] == False:
        prime.append(i)

#Aの素因数集合primeの倍数を全て除外する
for p in prime:
    for j in range(p*2, M+1, p):
        k[j] = False
    
ans = [1]

#kから答えを取り出す
for i in range(2, M+1):
    if k[i] == True:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)