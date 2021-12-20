H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

mod = 998244353

a = [0]
same_w = [0]
same_h = [0]
diff = [0]

def z_a(k):
    return (diff[k-2]*2 + same_w[k-2] * (H-2) + same_h[k-2] * (W-2) + a[k-2] * (W+H-2)) % mod

def z_same_w(k):
    return (same_w[k-1]*(H-2) + a[k-1] * (H-1) + diff[k-1]) % mod

def z_same_h(k):
    return (same_h[k-1]*(W-2) + a[k-1] * (W-1) + diff[k-1]) % mod

def z_diff(k):
    return (diff[k-1]*(H+W-4) + same_w[k-1]*(W-1) + same_h[k-1] * (H-1)) % mod


if x1 == x2 and y1 == y2:
    a[0] = 1
elif x1 == x2:
    same_h[0] = 1
elif y1 == y2:
    same_w[0] = 1
else:
    diff[0] = 1  

for i in range(1, K+1):
    if i == 1:
        a.append(same_h[0] + same_w[0])
        same_h.append(z_same_h(i))
        same_w.append(z_same_w(i))
        diff.append(z_diff(i))
    else:
        a.append(z_a(i))
        same_h.append(z_same_h(i))
        same_w.append(z_same_w(i))
        diff.append(z_diff(i))

print(a[-1])