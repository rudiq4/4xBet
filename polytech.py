#  Формула "Зовнішня швидкісна характеристика двигуна"
N = 112.66
g = 290
lst = []
kek = []
pimp = []
a = 0

for i in range(11):
    a = a + 600
    lst.append(a)
print(lst)

for i in lst:
    b = float(N*(i/6000+(i/6000)**2-(i/6000)**3))
    kek.append(b)
print(kek)

print('----<<<<<<<<<<______________>>>>>>>>>>--------')

for i in lst:
    c = float(g * (1.25-0.99*i/6000+0.98*(i/6000)**2)-0.24*(i/6000)**3)
    pimp.append(c)

print(pimp)





