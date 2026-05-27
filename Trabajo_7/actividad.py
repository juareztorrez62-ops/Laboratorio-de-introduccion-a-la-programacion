def clasificar_numero():
    clasificar = 0
    while clasificar == 0:
        numero = input("Ingrese un numero entero: ")
        if type(numero) == str and numero.lstrip("-").isdigit():
            numero = int(numero)

            if numero == 0:
                print("El numero es cero.")
            else:

                if numero > 0:
                    print("El numero es positivo.")

                elif numero < 0:
                    print("El numero es negativo.")

            if numero % 2 == 0 and numero != 0:
                print("El numero es par.")

            elif numero % 2 != 0 and numero != 0:
                print("El numero es impar.")

            clasificar = 1

        else:

            print("El valor ingresado no es un numero entero.")
            continue

        if clasificar == 1:

            print("¿Desea clasificar otro numero? (s/n)")

            respuesta = input().lower()

            if respuesta == "s":
                clasificar = 0

            else:
                break


def categoria_edad():

    print("Categoria de Edad y permisos.")

    print("Ingrese su edad (0 a 120)")
    edad = int(input())

    print("Cuenta con identificacion oficial? (s/n)")
    identificacion = input().lower()

    print("Cuenta con licencia de conducir? (s/n)")
    licencia = input().lower()

    if edad > 0 and edad < 12:
        print("Eres un niño.")

    elif edad > 12 and edad < 18:
        print("Eres un adolescente.")

    elif edad > 18 and edad < 64:
        print("Eres un adulto.")

    elif edad > 64 and edad < 120:
        print("Eres un adulto mayor.")

    else:
        print("Como sigues vivo?")

    if edad >= 13:
        print("Puedes registrarte")

    elif edad >= 13 and edad < 18:
        print("Puedes comprar con un tutor")

    else:
        print("Puedes comprar sin tutor")

    if edad >= 18 and licencia == "s":
        print("Puedes conducir")

    elif edad >= 21 and identificacion == "s":
        print("Puedes comprar servicio VIP")


def calcular_tarifa():

    print("Calcular tarifa.")

    precio_base = 200

    print("Ingrese su edad (0 a 120)")
    edad = int(input())

    print("Dia de la semana (1. Lunes a 7. Domingo)")
    dia = int(input())

    print("Es estudiante? (s/n)")
    estudiante = input().lower()

    print("Es miembro? (s/n)")
    miembro = input().lower()

    print("Metodo de pago efectivo o tarjeta (e/t)")
    metodo_pago = input().lower()

    if dia == 6 or dia == 7:
        recargo = precio_base * 0.10
    else:
        recargo = 0

    porcentaje_descuento = 0

    if 0 <= edad <= 120:

        if edad >= 0 and edad < 12:
            descuento_edad = precio_base * 0.50
            porcentaje_descuento = 50

        elif edad >= 13 and edad <= 17:
            descuento_edad = precio_base * 0.20
            porcentaje_descuento = 20

        elif edad >= 65:
            descuento_edad = precio_base * 0.30
            porcentaje_descuento = 30

        else:
            descuento_edad = 0

    else:
        print("Edad no válida.")

    if estudiante == "s" and edad <= 13:
        descuento_estudiante = precio_base * 0.15
        porcentaje_descuento += 15
    else:
        descuento_estudiante = 0

    if miembro == "s":
        descuento_miembro = precio_base * 0.10
        porcentaje_descuento += 10
    else:
        descuento_miembro = 0

    if metodo_pago == "e":
        descuento_pago = precio_base * 0.05
        porcentaje_descuento += 5
    else:
        descuento_pago = 0

    descuento_total = descuento_edad + descuento_estudiante + descuento_miembro + descuento_pago

    if porcentaje_descuento > 60:
        porcentaje_descuento = 60
        tarifa_final = precio_base + recargo - (precio_base * 0.60)

    else:
        tarifa_final = precio_base + recargo - descuento_total

    print("\nTarifa realizada")
    print("precio base:", precio_base)
    print("recargo:", recargo)
    print("Descuento aplicado:", porcentaje_descuento, "%")
    print("Descuento total:", descuento_total)
    print("Total final:", tarifa_final)

# login
intentos = 0

while intentos < 3:

    print("Usuario")
    usuario = input("Ingrese su nombre de usuario: ")

    print("Contraseña")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "":
        print("El usuario no puede estar vacío.")
        intentos += 1
        continue

    if not usuario.isalnum():
        print("El usuario debe ser alfanumérico.")
        intentos += 1
        continue

    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        intentos += 1
        continue

    tiene_letra = False
    tiene_numero = False

    for elemento in contraseña:

        if elemento.isalpha():
            tiene_letra = True

        if elemento.isdigit():
            tiene_numero = True

    if not tiene_letra or not tiene_numero:
        print("La contraseña debe contener una letra y un número.")
        intentos += 1
        continue

    if usuario == "admin" and contraseña == "Admin2026":
        print("Acceso concedido")
        acceso = 1

        while acceso == 1:
            print("\nMenú de opciones:")
            print("1. Clasificar numero")
            print("2. Categoria de Edad y permisos")
            print("3. Calcular tarifa")
            print("4. Cerrar sesion")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            match opcion:

                case "1":
                    clasificar_numero()

                case "2":
                    categoria_edad()

                case "3":
                    calcular_tarifa()

                case "4":
                    print("Cerrar sesion.")
                    acceso = 0

                case "5":
                    print("Saliendo del menú...")
                    intentos = 4
                    break

                case _:
                    print("Opción no válida.")

        break

    else:

        print("Credenciales incorrectas.")
        intentos += 1

if intentos == 3:
    print("Numero de intentos agotados.")

elif intentos == 4:
    print("Saliendo del sistema...")