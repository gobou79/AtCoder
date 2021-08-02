s_x, s_y, g_x, g_y = (int(x) for x in input().split())

G_y = - g_y

a = (s_y - G_y) / (s_x - g_x)

x = - s_y/a + s_x

print(x)