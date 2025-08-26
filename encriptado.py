import base64
import codecs
from unittest import result


def rot13(texto):
    return codecs.encode(texto, 'rot_13')

def caesar(texto, desplazamiento=3):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def base64_encode(texto):
    return base64.b64encode(texto.encode()).decode()

#estan todas las opciones
def encriptar(texto, opcion):
    if opcion == "1":   #rot13
        return rot13(texto)
    elif opcion == "2": #caesar
        return caesar(texto)
    elif opcion == "3": #base64
        return base64_encode(texto)
    elif opcion == "4": #todas
        return base64_encode(caesar(rot13(texto)))
    elif opcion == "5": #rot13 y caesar
        return caesar(rot13(texto))
    elif opcion == "6": #base64 y rot13
        return rot13(base64_encode(texto))
    elif opcion == "7": #esta el base64 y caesar
        return base64_encode(caesar(texto))
    else:
        return "Opción no válida."

#programa
print("Opciones de Encriptado:")
print("1. ROT13")
print("2. Caesar")
print("3. Base64")
print("4. ROT13 + Caesar + Base64")
print("5. ROT13 + Caesar")
print("6. Base64 + ROT13")
print("7. Caesar + Base64")

mensaje = input("\nIngresa el texto: ")
opcion = input("Elige una opción: ")

print("\nResultado:", result)
input("\nPresiona Enter para salir...")

resultado = encriptar(mensaje, opcion)
print("\nResultado:", resultado)
