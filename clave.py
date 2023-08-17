clave = int(input("ingrese su contraseña: "))
i = 0
if clave != 123:
     while clave != 123:
          clave = int(input("error, ingrese de nuevo: "))
          i=i+1
          if i > 1:
               print("muchos intentos, estas bloqueado")
               break
     else:
          print("bienvenido")


        
        

