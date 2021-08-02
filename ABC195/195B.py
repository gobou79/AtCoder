A, B, W = map(int, input().split())

w = W * 1000

c = w % A
a = w // A

if (B-A) * a < c:
    print("UNSATISFIABLE")
else:
    if w % B == 0:
        print(w//B, a)
    else:
        b = w//B+1
        print(b, a)