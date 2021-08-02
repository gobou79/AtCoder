T = int(input())

case = []
for _ in range(T):
    case.append(int(input()))

for i in case:
    if i % 4 == 0:
        print("Even")
    elif i % 2 == 0:
        print("Same")
    else:
        print("Odd")