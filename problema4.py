# PIDE INGRESAR EL ANGULO
angulo = int(input("Ingrese el numero del angulo: "))

if angulo == 0:
    print("nulo")
elif 0 < angulo < 90:  # angulo > 0 and angulo < 90
    print("agudo")
elif angulo == 90:
    print("recto")
elif 90 < angulo < 180:  # angulo > 90 and angulo < 180
    print("obtuso")
elif angulo == 180:
    print("llano")
elif 180 < angulo < 360:  # angulo > 180 and angulo < 360
    print("concavo")
elif angulo == 360:
    print("completo")
else:
    print("no encontrado")
