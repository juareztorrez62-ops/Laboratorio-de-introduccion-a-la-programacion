from unittest import case


def palabra():
    palabra = input("Ingresa una palabra: ")
    for i in range(0, 10):
        print(palabra)

def edad():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad != 0:
             for k in range (0, edad + 1):
                 print(k)    
        else:    
            print("Apenas naciste?")
    except ValueError:
        print("Edad no válida. Por favor, ingrese un número entero.")
        
def impares():
    try:
        numero = int(input("Ingrese un numero entero y positivo: "))
        if numero > 0:
            resultado = ""
            for i in range(0, numero +1 ):
                if i % 2 != 0:
                    resultado += str(i) + ", "
                    if i == numero or i == numero - 1:
                        resultado = resultado[:-2]
                    
                     
        print("Los numeros impares entre 0 y " + str(numero) + " son: " + resultado)            
    except ValueError:
        print("Numero no válido. Por favor, ingrese un número entero positivo.")

def cuenta_atras():
    try:
        numero = int(input("Ingrese un numero entero y positivo: "))
        if numero > 0:
            resultado = ""
            for i in range(numero, -1, -1):
                resultado += str(i) + ", "
                if i == 0:
                    resultado = resultado[:-2]
        print("Cuenta regresiva: " + resultado)
    except ValueError:
        print("Numero no válido. Por favor, ingrese un número entero positivo.")

def capital_obtenido():
    capital = float(input("Ingrese el valor del capital inicial: "))
    tasa = int(input("ingrese la tasa de interes anual (en porcentaje): "))
    años = int(input("Ingrese el numero de años: "))

    for i in range(1, años + 1):
        capital += capital * (tasa / 100)
        print(f"Capital al final del año {i}: {capital:.2f}")

def triangulo_rectangulo():
    altura = int(input("Ingrese la altura del triangulo: "))
    for i in range(1, altura + 1):
        print("*" * i)

def tabla_multiplicar():
    for i in range(1,11):
        for j in range(1,11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")

def piramide_numeros():
    numero = int(input("ingrese la altura de la piramide: "))
    for i in range(1, numero + 1):
        for j in range(2*i - 1, 0, - 2):
            print(j, end=" ")
        print()

def contraseña():
    contraseña = str(input("Ingrese una contraseña: "))
    ingresar_contraseña = str(input("ingrese la contraseña nuevamente: "))
    while contraseña != ingresar_contraseña:
        ingresar_contraseña = str(input("Contraseña incorrecta. Ingrese nuevamente:" ))
    print("Contraseña correcta.")

def numero_primo():
    num = int(input("ingrese un valor para saber si es primo o no :"))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} no es un numero primo.")
                break
        else:
            print(f"{num} es un numero primo.")
    else:
        print("Los numeros menores o iguales a 1 no son primos.")

def palabra_alrevez():
    palabra = input("ingrese una palabra. ")
    palabra_invertida = "" 
    for i in range(len(palabra) -1, -1, -1):
        palabra_invertida += palabra[i]
    print("La palabra alrevez es: " + palabra_invertida)

def frase_letra():
    frase = input("ingrese una frase: ")
    letra = input("ingrse una letra: ")
    contador = 0
    for i in range(len(frase)):
        if frase[i] == letra:
            contador += 1
    print(f"La letra '{letra}' aparece {contador} veces en la frase: {frase}")

def eco():
    while True:
        palabra = input("ingrese una palabra (o 'salir' para terminar): ")
        if palabra.lower() == "salir":
            print("Programa terminado.")
            break
        else:
            print(palabra)

while True:
    print("\nEjercicio 1: Imprimir una palabra 10 veces")
    print("Ejercicio 2: Imprimir los números del 0 a la edad ingresada")
    print("Ejercicio 3: Imprimir los números impares entre 0 y el número ingresado")   
    print("Ejercicio 4: Imprimir una cuenta regresiva desde el número ingresado hasta 0")
    print("Ejercicio 5: Calcular el capital obtenido después de un número de años con una tasa de interés anual")
    print("Ejercicio 6: Imprimir un triángulo rectángulo de asteriscos con la altura ingresada")
    print("Ejercicio 7: Imprimir la tabla de multiplicar del 1 al 10")
    print("Ejercicio 8: Imprimir una pirámide de números con la altura ingresada")
    print("Ejercicio 9: Verificar si una contraseña ingresada es correcta")            
    print("Ejercicio 10: Verificar si un número ingresado es primo o no")
    print("Ejercicio 11: Imprimir una palabra al revés")
    print("Ejercicio 12: Contar cuántas veces aparece una letra en una frase")
    print("Ejercicio 13: Programa de eco (repetir palabras hasta que se ingrese 'salir')")
    print(" '14'Salir del programa")
    opcion = input("Seleccione un ejercicio (1-13): ")

    match opcion:
        case "1":
            palabra()       
        case "2":
            edad()
        case "3":
            impares()
        case "4":
            cuenta_atras()  
        case "5":
            capital_obtenido()
        case "6":
            triangulo_rectangulo()
        case "7":
            tabla_multiplicar()
        case "8":
            piramide_numeros()
        case "9":
            contraseña()
        case "10":
            numero_primo()
        case "11":
            palabra_alrevez()
        case "12":
            frase_letra()
        case "13":
            eco()
        case "14":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, seleccione un número entre 1 y 13.")