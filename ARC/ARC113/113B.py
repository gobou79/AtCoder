A, B, C = map(int, input().split())

a = A % 10

amari = [[0], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]] 

b = B % len(amari[a])

c = C % len(amari[b])

e = amari[b][c]

print(amari[a][e])