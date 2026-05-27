numero_input = int(input("Ingresa un numero: "))

n = numero_input
if n == 0:
    binario = "0"
else:
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2

n = numero_input
if n == 0:
    octal = "0"
else:
    octal = ""
    while n > 0:
        residuo = n % 8
        octal = str(residuo) + octal
        n = n // 8

n = numero_input
if n == 0:
    hexadecimal = "0"
else:
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        residuo = n % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        n = n // 16

print("Binario:", binario)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)