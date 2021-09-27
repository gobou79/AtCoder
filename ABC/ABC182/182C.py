N = input()
mod = {}
mod[0] = 0
mod[1] = 0
mod[2] = 0

for i in range(len(N)):
    if int(N[i]) % 3 == 0:
        mod[0] += 1
    elif int(N[i]) % 3 == 1:
        mod[1] += 1
    else:
        mod[2] += 1

if int(N) % 3 == 0:
    print(0)
elif int(N) % 3 == 1:
    if mod[1] > 0 and len(N) > 1:
        print(1)
    elif mod[2] > 1 and len(N) > 2:
        print(2)
    else:
        print(-1)
else:
    if mod[2] > 0 and len(N) > 1:
        print(1)
    elif mod[1] > 1 and len(N) > 2:
        print(2)
    else:
        print(-1)
