# MOD
# 4 / 2 = 2 R = 0
# 4 % 2 = 0
# Cree un programa que me permita ingresar
# un numero y saber si este par o impar
# ** OJO: Recordar que el input() siempre guarda lo
# ** lo ingresa en un formato de tipo TEXTO (STRING)
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Numero es Par")
else:
    print("Numero es impar")
