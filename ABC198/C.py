import math

R, X, Y = map(int, input().split())

d = math.sqrt(X**2 + Y**2)

ans = math.ceil(d/R)

if (ans*R)**2 == X**2 + Y**2:
    print(ans)
elif ((ans-1)*R)**2 == X**2 + Y**2:
    print(ans-1)
elif ans == 1:
    print(ans+1)
else:
    print(ans)