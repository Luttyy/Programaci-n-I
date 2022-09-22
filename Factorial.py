numero =3
resultado = 1
resultado2 = 1
for x in range(1, numero + 1):
    resultado = resultado * x

while numero > 1:
    resultado2 *= numero   
    numero -= 1

print(resultado2)