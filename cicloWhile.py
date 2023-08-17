#la condicion se lee antes de empezar el ciclo y tambien antes de finalizar
respuesta = 1

while respuesta == 1:
    respuesta = int(input("1. Si\n2. No\n escriba el numero para continuar"))
    while respuesta != 1 and respuesta != 2:
        print("ingrese solo 1 o 2")
        respuesta = int(input("1. Si\n2. No\n escriba el numero para continuar"))
        if respuesta == 2:
            break

        