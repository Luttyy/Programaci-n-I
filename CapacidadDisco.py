cilindros = 12000 - int(input("Cilindros: "))
pistas = 16 - int(input("Pistas: "))
sectores = 8 - int(input("Sectores: "))
bytes = 512 -int(input("Bytes: "))

capacidad = int(cilindros * pistas * sectores * bytes)

print (capacidad)
