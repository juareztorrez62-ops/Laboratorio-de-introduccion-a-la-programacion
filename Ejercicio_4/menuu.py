# Contador de intentos fallidos
intentos = 0

# Número máximo de intentos permitidos
intentos_maximos = 3

# Estado de acceso
acceso_concedido = False

# Credenciales válidas
usuario_valido = "admin"
password_valido = "Admin2026"

# Control general del programa
ejecutando_programa = True


# Bucle principal
while ejecutando_programa:

    # LOGIN
    while intentos < intentos_maximos and not acceso_concedido:

        print("\n--- INICIAR SESION ---")

        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        valido = True

        # Validar usuario
        if usuario == "":
            print("El usuario no debe estar vacío.")
            valido = False

        elif not usuario.isalnum():
            print("El usuario no debe tener espacios.")
            valido = False

        # Validar contraseña
        if len(contraseña) < 8:
            print("La contraseña debe tener mínimo 8 caracteres.")
            valido = False

        # Verificar letra
        tiene_letra = False

        for char in contraseña:
            if char.isalpha():
                tiene_letra = True
                break

        if not tiene_letra:
            print("La contraseña debe tener al menos una letra.")
            valido = False

        # Verificar número
        tiene_numero = False

        for char in contraseña:
            if char.isdigit():
                tiene_numero = True
                break

        if not tiene_numero:
            print("La contraseña debe tener al menos un número.")
            valido = False

        # Verificar credenciales
        if valido:

            if usuario == usuario_valido and contraseña == password_valido:

                print("\nAcceso permitido.\n")

                acceso_concedido = True

                # Reiniciar intentos
                intentos = 0

            else:
                intentos += 1

                print("Datos incorrectos.")
                print("Intentos restantes:", intentos_maximos - intentos)

        else:
            print("Datos inválidos.\n")

    # Bloqueo por intentos
    if intentos == intentos_maximos:
        print("\nSe alcanzó el número máximo de intentos.")
        ejecutando_programa = False

    # MENU
    while acceso_concedido:

        print("\n--- MENU ---")
        print("1) Clasificar números")
        print("2) Categoría de edad y permisos")
        print("3) Calcular tarifa final")
        print("4) Cerrar sesión")
        print("5) Salir")

        opcion = input("Seleccione una opción: ")

        # OPCIONES
        if opcion == "1":
            print("Entraste a Clasificar números")

        elif opcion == "2":
            print("Entraste a Categoría de edad")

        elif opcion == "3":
            print("Entraste a Calcular tarifa")

        elif opcion == "4":
            print("Sesión cerrada.")

            acceso_concedido = False

        elif opcion == "5":
            print("Programa finalizado.")

            acceso_concedido = False
            ejecutando_programa = False

        else:
            print("Opción inválida.")