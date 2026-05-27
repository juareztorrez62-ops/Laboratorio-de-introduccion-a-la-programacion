intentos = 0
intentos_Maximos = 3
acceso_concedido = False
usuario_valido = "admin"
password_valido = "Admin2026"
ejecutando_programa = True

while ejecutando_programa:
    
    while intentos < intentos_Maximos and not acceso_concedido:
        print("INICIAR SESION")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        valido = True   

        if usuario == "":
            print("El usuario no debe estar vacio")
            valido = False
        elif not usuario.isalnum():
            print("El usuario no debe tener espacios.")
            valido = False
        
        if len(contraseña) < 8:
            print("Contraseña debe tener minimo 8 caracteres.")
            valido = False

        tiene_letra = False
        for char in contraseña:
            if char.isalpha():
                tiene_letra = True
                break
        if not tiene_letra:
            print("La contraseña debe tener al menos una letra")
            valido = False

        tiene_numero = False
        for char in contraseña:
            if char.isdigit():
                tiene_numero = True
                break
        if not tiene_numero:
            print("La contraseña debe tener al menos un numero")
            valido = False

        if valido:
            if usuario == usuario_valido and contraseña == password_valido:
                print("Acceso permitido\n")
                acceso_concedido = True
            else:
                intentos += 1
                print("Datos incorrectos.")
                print("Tienes", intentos_Maximos - intentos, "intentos\n")
        else:
            print("Datos incorrectos, intenta de nuevo\n")

    if intentos == intentos_Maximos:
        print("Se alcanzo el numero de intentos permitidos. Programa terminado.")
        ejecutando_programa = False

    while acceso_concedido:
        print("---MENU---")
        print("1) Clasificar números")
        print("2) Categoría de edad y permisos")
        print("3) Calcular tarifa final")
        print("4) Cerrar sesión")
        print("5) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n[Clasificar números]")
            num_check = int(input("Ingresa un numero: "))
            if num_check > 0:
                print("El numero es positivo")
            elif num_check < 0:
                print("El numero es negativo")
            else:
                print("El numero es cero")
            
            if num_check % 2 == 0:
                print("El numero es par")
            else:
                print("El numero es impar")

        elif opcion == "2":
            while True: 
                print("\n[Categoria de edad y permisos]")
                edad = int(input("Ingresa tu edad (0 a 120): "))
                if edad < 0 or edad > 120:
                    print("Edad no válida.")
                    break
                
                ide = input("¿Cuenta con identificación? (s/n): ").lower()
                lic = input("¿Cuenta con licencia de conducir? (s/n): ").lower()

                if 0 <= edad <= 12:
                    print(f"Edad: {edad}. Eres un niño, necesitas tutor.")
                elif 13 <= edad <= 17:
                    print(f"Edad: {edad}. Eres adolescente, necesitas tutor.")
                elif 18 <= edad <= 64:
                    print(f"Edad: {edad}. Eres adulto.")
                    if edad >= 21 and ide == "s":
                        print("Acceso VIP disponible.")
                else:
                    print(f"Edad: {edad}. Eres adulto mayor.")
                    if ide == "s":
                        print("Acceso VIP disponible.")

                if lic == "s":
                    print("Puedes conducir.")
                else:
                    print("No puedes conducir.")

                resp = input("\n1. Reiniciar proceso / 2. Volver al menu: ")
                if resp != "1":
                    break

        elif opcion == "3":
            print("\n[Calcular tarifa final] - Seccion en desarrollo...")

        elif opcion == "4":
            print("Cerrando sesion...\n")
            acceso_concedido = False
            intentos = 0 

        elif opcion == "5":
            print("Saliendo del programa.")
            acceso_concedido = False
            programa_activo = False
        else:
            print("Opcion invalida.")