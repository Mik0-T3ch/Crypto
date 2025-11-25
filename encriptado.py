import base64
import codecs

# ------------------- FUNCIONES DE ENCRIPTADO -------------------

def rot13(texto):
    return codecs.encode(texto, 'rot_13')

def caesar(texto, desplazar=3):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazar) % 26 + base)
        else:
            resultado += c
    return resultado

def base64_encode(texto):
    return base64.b64encode(texto.encode()).decode()

# ------------------- MORSE -------------------

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'
}

EXPLICACION = {
    'A': 'Asno', 'B': 'Burro', 'C': 'Casa', 'D': 'Dedo', 'E': 'Elefante',
    'F': 'Foca', 'G': 'Gato', 'H': 'Hola', 'I': 'Isla', 'J': 'Jugo',
    'K': 'Kilo', 'L': 'Luna', 'M': 'Mano', 'N': 'Nube', 'O': 'Oso',
    'P': 'Pato', 'Q': 'Queso', 'R': 'Ratón', 'S': 'Sol', 'T': 'Taza',
    'U': 'Uva', 'V': 'Vaca', 'W': 'Wifi', 'X': 'Xilófono', 'Y': 'Yate', 'Z': 'Zorro'
}

def morse_diccionario():
    # Historia detallada
    contenido = "--- Historia del Código Morse ---\n\n"
    contenido += (
        "El código Morse fue inventado en 1837 por Samuel Morse y Alfred Vail.\n"
        "Su objetivo era transmitir mensajes de texto a larga distancia usando telégrafo.\n"
        "Cada letra y número tiene un código único de puntos (.) y rayas (-).\n"
        "Se utilizó en comunicaciones militares, marítimas y radioaficionados,\n"
        "y fue un estándar de comunicación hasta la llegada de tecnologías modernas.\n\n"
    )

    # Diccionario en varias columnas para mejor visualización
    contenido += "--- Diccionario Morse Educativo ---\n\n"
    filas = []
    for letra in sorted(MORSE.keys()):
        palabra = EXPLICACION.get(letra, '')
        codigo = MORSE[letra]
        filas.append(f"{letra} = {palabra:<10} Morse: {codigo}")

    # Agrupar en 2 o 3 columnas por línea
    columnas = 3
    for i in range(0, len(filas), columnas):
        contenido += " | ".join(filas[i:i+columnas]) + "\n"

    contenido += "\nExplicación: Cada letra tiene un código único de puntos (.) y rayas (-).\n"
    contenido += "Los espacios entre letras se representan con un espacio y entre palabras con '/'.\n"

    return contenido

# ------------------- DICCIONARIO DE OPCIONES -------------------
opciones = {
    "1": rot13,
    "2": caesar,
    "3": base64_encode,
    "4": lambda texto: base64_encode(caesar(rot13(texto))),
    "5": lambda texto: caesar(rot13(texto)),
    "6": lambda texto: rot13(base64_encode(texto)),
    "7": lambda texto: base64_encode(caesar(texto)),
    "8": morse_diccionario
}

# ------------------- PROGRAMA -------------------
print("Opciones de Encriptado:")
print("1. ROT13")
print("2. Caesar")
print("3. Base64")
print("4. ROT13 + Caesar + Base64")
print("5. ROT13 + Caesar")
print("6. Base64 + ROT13")
print("7. Caesar + Base64")
print("8. Morse (diccionario completo)")

opcion = input("\nElige una opción: ")

if opcion in opciones:
    resultado = opciones[opcion]()  # si es Morse, retorna toda la info
    print("\n" + resultado)  # se muestra todo junto
else:
    print("Opción no válida")

input("\nPresiona Enter para salir...")
